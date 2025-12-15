#!/usr/bin/env python3
"""
Test script to verify the RAG retrieval validation functionality
"""
import sys
import os

# Add the current directory to the path so we can import main.py
sys.path.append(os.path.dirname(__file__))

from main import validate_qdrant_connection, validate_cohere_connection, test_with_sample_queries

def test_validation_functionality():
    """Test the validation functionality"""
    print("Testing RAG Retrieval Validation Functionality...")

    # Test 1: Validate connections
    print("\n1. Testing connections...")
    qdrant_ok = validate_qdrant_connection()
    cohere_ok = validate_cohere_connection()

    print(f"   Qdrant connection: {'PASS' if qdrant_ok else 'FAIL'}")
    print(f"   Cohere connection: {'PASS' if cohere_ok else 'FAIL'}")

    if not (qdrant_ok and cohere_ok):
        print("   Cannot proceed with validation - connection issues detected")
        return False

    # Test 2: Run sample queries
    print("\n2. Testing sample queries...")
    try:
        results, report = test_with_sample_queries()
        print(f"   Sample query testing: PASS ({len(results)} queries processed)")
        print(f"   Sample results: {len(results)} queries with {sum(len(r.results) for r in results)} total results")
    except Exception as e:
        print(f"   Sample query testing: FAIL ({str(e)})")
        return False

    print("\n3. All validation tests completed successfully! PASS")
    return True

if __name__ == "__main__":
    success = test_validation_functionality()
    if success:
        print("\nPASS: RAG retrieval validation system is working correctly!")
        sys.exit(0)
    else:
        print("\nFAIL: RAG retrieval validation system has issues!")
        sys.exit(1)