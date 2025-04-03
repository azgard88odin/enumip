import argparse
import json
import requests
import re
try:
    from colorama import init, Fore
    COLORAMA_AVAILABLE = True
except ImportError:
    COLORAMA_AVAILABLE = False
    print("For colored output, install colorama: pip install colorama")

def read_ips_from_file(file_path):
    """Read IP addresses from a file, one per line."""
    try:
        with open(file_path, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"Error reading IP file: {e}")
        return []

def print_colored_json(json_data):
    """Print JSON with color formatting."""
    if not COLORAMA_AVAILABLE:
        print(json.dumps(json_data, indent=4))
        return
    
    # Convert to string with indentation
    json_str = json.dumps(json_data, indent=4)
    
    # Color patterns
    json_str = re.sub(
        r'"([^"]+)":', 
        f"{Fore.CYAN}\"\\1\"{Fore.RESET}:", 
        json_str
    )
    json_str = re.sub(
        r': "([^"]+)"', 
        f": {Fore.GREEN}\"\\1\"{Fore.RESET}", 
        json_str
    )
    json_str = re.sub(
        r': (true|false)', 
        f": {Fore.YELLOW}\\1{Fore.RESET}", 
        json_str
    )
    json_str = re.sub(
        r': (-?\d+(?:\.\d+)?)', 
        f": {Fore.MAGENTA}\\1{Fore.RESET}", 
        json_str
    )
    print(json_str)

def main():
    # Initialize colorama if available
    if COLORAMA_AVAILABLE:
        init()
    
    parser = argparse.ArgumentParser(description='Query ip-api for IP info.')
    parser.add_argument('ips', nargs='*', help='One or more IP addresses')
    parser.add_argument('--input', '-i', type=str, help='Input file with IP addresses (one per line)')
    parser.add_argument('--output', '-o', type=str, help='Output file path (optional)')
    args = parser.parse_args()

    # Gather IPs from command line
    all_ips = list(args.ips)
    
    # If input file is provided, read IPs from it
    if args.input:
        file_ips = read_ips_from_file(args.input)
        all_ips.extend(file_ips)
    
    if not all_ips:
        print("No IP addresses provided. Use positional arguments or --input/-i option.")
        return

    if len(all_ips) == 1:
        # Single IP request
        url = f'http://ip-api.com/json/{all_ips[0]}?fields=66846719'
        response = requests.get(url)
    else:
        # Multiple IPs request
        url = 'http://ip-api.com/batch?fields=66842623'
        response = requests.post(url, json=all_ips)

    try:
        data = response.json()
    except Exception as e:
        if COLORAMA_AVAILABLE:
            print(f"{Fore.RED}Error reading response JSON: {e}{Fore.RESET}")
        else:
            print(f"Error reading response JSON: {e}")
        return

    if args.output:
        try:
            with open(args.output, 'w') as f:
                f.write(json.dumps(data, indent=4))
            if COLORAMA_AVAILABLE:
                print(f"{Fore.GREEN}Results written to {args.output}{Fore.RESET}")
            else:
                print(f"Results written to {args.output}")
        except Exception as e:
            if COLORAMA_AVAILABLE:
                print(f"{Fore.RED}Error writing to output file: {e}{Fore.RESET}")
            else:
                print(f"Error writing to output file: {e}")
    else:
        print_colored_json(data)

if __name__ == '__main__':
    main()
