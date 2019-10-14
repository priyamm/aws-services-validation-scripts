## Requirements
- python 3
- boto3
- aws cli

## Instructions
 - For a particular bucket "example_bucket"
```bash
python script.py example_bucket
```
And it will return 0 if not READ, READ_ACP or WRITE

- For all buckets 
```bash
python script.py all_buckets
```
