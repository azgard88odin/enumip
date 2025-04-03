# IP Enumeration Tool (EnumIP)

## Overview

`enumip.py` is a powerful tool for passive reconnaissance that allows cybersecurity and OSINT professionals to quickly gather geographical and network information about IP addresses. This tool leverages the ip-api.com API to retrieve comprehensive data about target IPs, making it invaluable during the initial footprinting and passive reconnaissance phases of security assessments.

## Features

- Query detailed information for a single IP address or multiple IPs simultaneously
- Process IP addresses from command line arguments or input files
- Optional colored output for better visualization (requires colorama)
- Export results to JSON files for further analysis or reporting
- Batch processing capability to handle large numbers of targets efficiently

## Installation

### Prerequisites

- Python 3.x
- Required Python packages:
  - requests
  - argparse
  - json (standard library)
  - re (standard library)
  - colorama (optional, for colored output)

### Setting up

1. Ensure Python 3.x is installed on your system
2. Install required dependencies:

```bash
pip install requests colorama
```

## Usage

### Basic Usage

Query a single IP address:

```bash
python enumip.py 8.8.8.8
```

Query multiple IP addresses:

```bash
python enumip.py 8.8.8.8 1.1.1.1 9.9.9.9
```

### Advanced Usage

Read IP addresses from a file:

```bash
python enumip.py --input targets.txt
```

Save results to an output file:

```bash
python enumip.py 8.8.8.8 --output results.json
```

Combine input file and command line IPs:

```bash
python enumip.py 8.8.8.8 --input additional_targets.txt
```

Process a list and save results:

```bash
python enumip.py --input target_list.txt --output reconnaissance_results.json
```

## Output Information

The tool queries the following information for each IP address (fields may vary based on IP-API's response):

- Geographic data (country, region, city, zip, latitude, longitude)
- Network information (ISP, organization, ASN)
- Security-relevant details (proxy/VPN detection, hosting status)
- Time zone information

## Example Output

```json
{
    "status": "success",
    "country": "United States",
    "countryCode": "US",
    "region": "VA",
    "regionName": "Virginia",
    "city": "Ashburn",
    "zip": "20149",
    "lat": 39.03,
    "lon": -77.5,
    "timezone": "America/New_York",
    "isp": "Google LLC",
    "org": "Google Public DNS",
    "as": "AS15169 Google LLC",
    "query": "8.8.8.8"
}
```

## Use Cases in Cybersecurity and OSINT

- **Initial Reconnaissance**: Gather basic information about target infrastructures
- **Threat Intelligence**: Identify potentially malicious IPs by examining hosting details
- **Attack Surface Mapping**: Understand the geographic and network distribution of targets
- **Incident Response**: Quickly analyze suspicious IP addresses involved in security incidents
- **Threat Hunting**: Collect data about suspicious IPs for deeper investigation

## Legal and Ethical Considerations

This tool should only be used for:
- Authorized security assessments
- Defensive security research
- Educational purposes
- Targets where you have explicit permission to perform reconnaissance

Always adhere to applicable laws and regulations when conducting security assessments or OSINT operations.

## API Rate Limits

The ip-api.com free tier has usage limitations:
- 45 requests per minute
- Consider implementing delays for large batches of IPs
- For commercial or high-volume usage, consider their paid services

## Notes

- All data is retrieved from ip-api.com and its accuracy depends on their database
- The information obtained is publicly available through the IP-API service
- For colored output, ensure the colorama package is installed
