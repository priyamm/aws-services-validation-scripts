import boto3
import sys

class S3ACL:
    def __init__(self):
        self.s3 = boto3.client('s3')
    
    def bucket_has_read_write(self,bucket_name):
        # Verify whether read and write access is present
        permission = self.s3.get_bucket_acl(
                Bucket=bucket_name
            )
        for p in permission['Grants']:
            if 'READ' in p['Permission']:
                return 'READ' 
            if 'READ_ACP' in p['Permission']:
                return 'READ_ACP'
            if 'WRITE' in p['Permission']:
                return 'WRITE'
        return 0

    
    def all_bucket_acl_permissions(self):
        # Print all access control policy for each bucket
        bucket_list = self.s3.list_buckets()['Buckets']
        for bucket in bucket_list:
            bucket_name = bucket['Name']
            permission = self.s3.get_bucket_acl(
                Bucket=bucket_name
            )
            permissions = '|'.join([p['Permission'] for p in permission['Grants']])
            print("Bucket name: {}, Permission: {}".format(bucket_name,permissions))



if __name__ == "__main__":
    if len (sys.argv) == 2 :
        s3_acl = S3ACL()
        if "all_buckets" == sys.argv[1]:
            s3_acl.all_bucket_acl_permissions()
        else: 
            r = s3_acl.bucket_has_read_write(sys.argv[1]) 
            print(r)
    else:
        print("Usage: \n - python script.py <bucket_name> \n - python script.py all_buckets")



    

