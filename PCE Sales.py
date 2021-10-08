# Databricks notebook source
# MAGIC %python
# MAGIC print("Connecting To Mintel Container in Azure Blob Storage")
# MAGIC storage_account_name="bnlwestgunileverbd00009"
# MAGIC storage_account_key="EKEANQvK6dov59asKbKiD6BQqFZXW8/wXCdOK+h9avJ+TCQ4VU0y6QrVvK/eZ4M8r5/V8exCzg8ozVjeI2x4Gg=="
# MAGIC container="mintel"
# MAGIC 
# MAGIC spark.conf.set(f"fs.azure.account.key.{storage_account_name}.blob.core.windows.net", storage_account_key)
# MAGIC print('Unmounting all mounts beginning with /mnt/')
# MAGIC dbutils.fs.mounts()
# MAGIC for mount in dbutils.fs.mounts():
# MAGIC   if mount.mountPoint.startswith('/mnt/'):
# MAGIC     dbutils.fs.unmount(mount.mountPoint)
# MAGIC 
# MAGIC print('Re-listing all mounts')
# MAGIC dbutils.fs.mounts()
# MAGIC 
# MAGIC print("Mounting Container onto DataBricks from Azure Blob Storage")
# MAGIC try:
# MAGIC   dbutils.fs.mount(
# MAGIC   source=f"wasbs://{container}@{storage_account_name}.blob.core.windows.net/",
# MAGIC   mount_point="/mnt/storage",
# MAGIC   extra_configs={f"fs.azure.account.key.{storage_account_name}.blob.core.windows.net": storage_account_key}
# MAGIC   )
# MAGIC except:
# MAGIC   print("Already Mounted")
# MAGIC 
# MAGIC print("The files currently present in the container are")
# MAGIC dbutils.fs.ls(f"wasbs://{container}@{storage_account_name}.blob.core.windows.net/")
