import os
from moviepy.editor import ImageSequenceClip

def create_gif(image_files, output_gif, duration=0.5):
    """
    Create a GIF from a list of image files.

    Args:
        image_files (list): List of image file paths.
        output_gif (str): Output GIF filename.
        duration (float): Duration (in seconds) between frames.

    Returns:
        None
    """
    clip = ImageSequenceClip(image_files, fps=1 / duration)
    clip.write_videofile(output_gif, fps=1 / duration, codec='gif', audio=False)

def collect_images_from_directory(directory):
    """
    Collect image files (PNG and JPG) from a directory.

    Args:
        directory (str): Directory path.

    Returns:
        list: List of image file paths.
    """
    image_files = []
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_files.append(os.path.join(directory, filename))
    return sorted(image_files)

def main():
    print("Welcome to the Image to GIF Converter!")
    
    # Ask the user for input directory and output GIF filename
    input_directory = input("Enter the directory containing image files: ")
    output_gif_filename = input("Enter the output GIF filename (e.g., output.gif): ")

    # Collect image files from the specified directory
    image_files = collect_images_from_directory(input_directory)

    if not image_files:
        print("No image files found in the specified directory.")
    else:
        try:
            # Ask the user for the frame duration
            duration = float(input("Enter the duration between frames (in seconds): "))

            # Create the GIF with a specified duration
            create_gif(image_files, output_gif_filename, duration)
            print(f"GIF saved as {output_gif_filename}")
        except ValueError:
            print("Invalid duration input. Please enter a valid number in seconds.")

if __name__ == "__main__":
    main()
