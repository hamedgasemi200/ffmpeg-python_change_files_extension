import glob, os, ntpath

# Get the directory of the files
directory = input('Enter directory\n').rstrip('/')

# Get default extension
from_extension = input("Change extension from:\n")

# Get wanted extension
new_extension = input("Enter new extension:\n")

# Get ffmpeg path
ffmpeg_binary = input("Enter the path of the ffmpeg binary (default ffmpeg)\n")
if not ffmpeg_binary: ffmpeg_binary = 'ffmpeg'

# Get files
files = glob.glob('{}/*.{}'.format(directory, from_extension))

# Iterate through the files
for file_path in files:
    # Get file name, and extension
    name, extension = ntpath.basename(file_path).split('.')

    # Generate FFMPEG command
    ffmpeg_command = '{0} -i "{1}/{2}.{3}" "{1}/{2}.{4}" -y'.format(ffmpeg_binary, directory, name, from_extension,
                                                                    new_extension)

    print(ffmpeg_command)
    # Run the command
    os.popen(ffmpeg_command)
