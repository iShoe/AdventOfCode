# Snippet

def get_lines(file_path):
    with open(file_path) as f:
        lines = f.read().strip().split('\n')
        return lines

