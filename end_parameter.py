def set_end_parameter(text, end="\n"):
    """
    Sets the end parameter for text output.
    
    Args:
        text (str): The text to be printed
        end (str): The ending character(s) to append to the text (default: newline)
    
    Returns:
        str: Text with the specified ending
    """
    return f"{text}{end}"

# Example usage
if __name__ == "__main__":
    # Print with default newline ending
    print(set_end_parameter("Hello"))  # Output: Hello\n
    
    # Print with custom ending
    print(set_end_parameter("Hello", end=" "))  # Output: Hello 
    print(set_end_parameter("World", end="!"))  # Output: World!
    
    # Print without any ending
    print(set_end_parameter("No ending", end=""))  # Output: No ending
