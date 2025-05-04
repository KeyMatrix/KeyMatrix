import json
import sys

def validate_filter(filter_path, artifact_path):
    try:
        with open(filter_path, 'r') as filter_file:
            guardian_filter = json.load(filter_file)

        with open(artifact_path, 'r') as artifact_file:
            artifacts = json.load(artifact_file)

        for artifact in artifacts.get("artifacts", []):
            for rule in guardian_filter["rules"]:
                condition = rule["condition"]
                if eval(condition):  # Простая эмуляция проверки
                    print(f"Rejected: {rule['message']}")
                    sys.exit(1)

        print("Validation passed. All artifacts are valid.")
    except Exception as e:
        print(f"Error during validation: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python validate_filter.py <filter_path> <artifact_path>")
        sys.exit(1)

    filter_path = sys.argv[1]
    artifact_path = sys.argv[2]
    validate_filter(filter_path, artifact_path)