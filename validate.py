#!/usr/bin/env python3
"""
Validation script for TrueNAS Core 13 plugin index
Validates JSON syntax, INDEX file, and plugin manifests
"""

import json
import sys
import os
from pathlib import Path

def validate_json_file(filepath):
    """Validate JSON syntax of a file"""
    try:
        with open(filepath, 'r') as f:
            json.load(f)
        return True, None
    except json.JSONDecodeError as e:
        return False, str(e)
    except Exception as e:
        return False, str(e)

def validate_index_schema(index_data):
    """Validate INDEX file structure"""
    required_fields = ['MANIFEST', 'name', 'icon', 'description', 'official', 'primary_pkg']
    errors = []
    
    for plugin_name, plugin_data in index_data.items():
        for field in required_fields:
            if field not in plugin_data:
                errors.append(f"Plugin '{plugin_name}' missing required field: {field}")
    
    return errors

def validate_manifest_file(manifest_path, plugin_name):
    """Validate plugin manifest structure"""
    required_fields = ['name', 'release', 'artifact', 'official']
    warnings = []
    errors = []
    
    valid, error = validate_json_file(manifest_path)
    if not valid:
        errors.append(f"Manifest {manifest_path} has invalid JSON: {error}")
        return errors, warnings
    
    with open(manifest_path, 'r') as f:
        manifest = json.load(f)
    
    # Check required fields
    for field in required_fields:
        if field not in manifest:
            errors.append(f"Manifest {manifest_path} missing required field: {field}")
    
    # Check release version
    if 'release' in manifest:
        release = manifest['release']
        if '13.' not in release:
            warnings.append(f"{plugin_name}: Using release {release} (expected 13.x-RELEASE)")
    
    # Check artifact URL
    if 'artifact' in manifest:
        artifact = manifest['artifact']
        if not artifact.startswith('https://'):
            warnings.append(f"{plugin_name}: Artifact URL should use HTTPS: {artifact}")
    
    return errors, warnings

def main():
    """Main validation routine"""
    print("=" * 70)
    print("TrueNAS Core 13 Plugin Index Validator")
    print("=" * 70)
    print()
    
    all_errors = []
    all_warnings = []
    
    # Validate INDEX file
    print("[1/4] Validating INDEX file...")
    index_path = 'INDEX'
    if not os.path.exists(index_path):
        print(f"✗ ERROR: {index_path} file not found!")
        return 1
    
    valid, error = validate_json_file(index_path)
    if not valid:
        print(f"✗ ERROR: INDEX file has invalid JSON syntax: {error}")
        return 1
    
    with open(index_path, 'r') as f:
        index_data = json.load(f)
    
    print(f"✓ INDEX file loaded successfully ({len(index_data)} plugins)")
    
    # Validate INDEX structure
    print("\n[2/4] Validating INDEX structure...")
    schema_errors = validate_index_schema(index_data)
    if schema_errors:
        all_errors.extend(schema_errors)
        for error in schema_errors:
            print(f"  ✗ {error}")
    else:
        print("✓ INDEX structure is valid")
    
    # Validate all plugin manifest files
    print("\n[3/4] Validating plugin manifest files...")
    for plugin_name, plugin_data in index_data.items():
        manifest_file = plugin_data['MANIFEST']
        
        if not os.path.exists(manifest_file):
            error = f"Manifest file {manifest_file} not found for plugin '{plugin_name}'"
            all_errors.append(error)
            print(f"  ✗ {error}")
            continue
        
        errors, warnings = validate_manifest_file(manifest_file, plugin_name)
        if errors:
            all_errors.extend(errors)
            for error in errors:
                print(f"  ✗ {error}")
        if warnings:
            all_warnings.extend(warnings)
            for warning in warnings:
                print(f"  ⚠ {warning}")
        
        if not errors and not warnings:
            print(f"  ✓ {plugin_name} ({manifest_file})")
    
    # Validate all JSON files in root
    print("\n[4/4] Validating all JSON files...")
    json_files = [f for f in os.listdir('.') if f.endswith('.json')]
    for json_file in json_files:
        valid, error = validate_json_file(json_file)
        if valid:
            print(f"  ✓ {json_file}")
        else:
            all_errors.append(f"{json_file}: {error}")
            print(f"  ✗ {json_file}: {error}")
    
    # Summary
    print("\n" + "=" * 70)
    print("VALIDATION SUMMARY")
    print("=" * 70)
    
    if all_warnings:
        print(f"\n⚠ Warnings: {len(all_warnings)}")
        for warning in all_warnings:
            print(f"  - {warning}")
    
    if all_errors:
        print(f"\n✗ Errors: {len(all_errors)}")
        for error in all_errors:
            print(f"  - {error}")
        print("\n✗ VALIDATION FAILED")
        return 1
    else:
        if all_warnings:
            print("\n⚠ VALIDATION PASSED WITH WARNINGS")
        else:
            print("\n✓ VALIDATION PASSED")
        return 0

if __name__ == '__main__':
    sys.exit(main())
