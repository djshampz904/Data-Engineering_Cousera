current_date=$(date +%Y%m%d)

# Set the filename for the backup
backup_filename="all-databases-backup-${current_date}.sql"

# Set the directory for the backup
backup_directory="/tmp/mysqldumps/${current_date}"

# Create the destination directory if it doesn't exist
mkdir -p $backup_directory

# If directory creation failed, exit the script
if [ $? -ne 0 ]; then
    echo "Failed to create directory $backup_directory. Exiting."
    exit 1
fi

# Backup all databases using mysqldump
mysqldump --all-databases --user=root > "$backup_directory/$backup_filename"

# If mysqldump failed, remove the directory and exit the script
if [ $? -ne 0 ]; then
    echo "Backup failed. Removing directory $backup_directory."
    rm -r $backup_directory
    exit 1
fi