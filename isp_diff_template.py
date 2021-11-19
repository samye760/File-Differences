IDENTICAL = -1

def singleline_diff(line1, line2):
    
    """
    Inputs:
        line1 - first single line string
        line2 - second single line string
    Output:
        Returns the index where the first difference between
        line1 and line2 occurs.
        Returns IDENTICAL if the two lines are the same.
    """
 
    if len(line1) > len(line2):
        for idx in range(len(line2)):
            if line1[idx] != line2[idx]:
                return idx
        return len(line2)

    elif len(line2) > len(line1):
        for idx in range(len(line1)):
            if line1[idx] != line2[idx]:
                return idx
        return len(line1)

    else:
        for idx in range(len(line1)):
            if line1[idx] != line2[idx]:
                return idx
        return IDENTICAL 

def singleline_diff_format(line1, line2, idx):
    
    """
    Inputs:
        line1 - first single line string
        line2 - second single line string
        idx   - index at which to indicate difference
    Output:
        Returns a three line formatted string showing the location
        of the first difference between line1 and line2.

        If either input line contains a newline or carriage return,
        then returns an empty string.

        If idx is not a valid index, then returns an empty string.
    """
    strng = ""
 
    if "/n" in line1 or "/r" in line1 or "/n" in line2 or "/r" in line2:
        return ""
    elif (idx > len(line1) or idx > len(line2)) or idx < 0:
        return ""
    else:
        for counter in range(idx):
            strng += "="
            counter += 0
   
    strng += "^"
 
    return f"{line1}\n{strng}\n{line2}\n"

def multiline_diff(lines1, lines2):
    
    """
    Inputs:
        lines1 - list of single line strings
        lines2 - list of single line strings
    Output:
        Returns a tuple containing the line number (starting from 0) and
        the index in that line where the first difference between lines1
        and lines2 occurs.

        Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
 
    if len(lines1) > len(lines2):
        for line in range(len(lines2)):
            diff = singleline_diff(lines1[line], lines2[line])
            if diff != -1:
                return (line, diff)
        return (len(lines2), 0)

    elif len(lines2) > len(lines1):
        for line in range(len(lines1)):
            diff = singleline_diff(lines1[line], lines2[line])
            if diff != -1:
                return (line, diff)
        return (len(lines1), 0)

    else:
        for line in range(len(lines1)):
            diff = singleline_diff(lines1[line], lines2[line])
            if diff != -1:
                return (line, diff)
        return (IDENTICAL, IDENTICAL)

def get_file_lines(filename):
    """
    Inputs:
        filename - name of file to read
    Output:
        Returns a list of lines from the file named filename.  Each
        line will be a single line string with no newline ('\n') or
        return ('\r') characters.

        If the file does not exist or is not readable, then the
        behavior of this function is undefined.
    """
    with open(filename, "rt") as filen:
        lines = []
        for line in filen:
            line = line.replace("\n", "").replace("\r", "")
            lines.append(line)
   
    return lines

def file_diff_format(filename1, filename2):
    """
    Inputs:
        filename1 - name of first file
        filename2 - name of second file
    Output:
        Returns a four line string showing the location of the first
        difference between the two files named by the inputs.

        If the files are identical, the function instead returns the
        string "No differences\n".

        If either file does not exist or is not readable, then the
        behavior of this function is undefined.
    """
    fn1 = get_file_lines(filename1)
    fn2 = get_file_lines(filename2)
    diff = multiline_diff(fn1, fn2)
    if diff == (IDENTICAL, IDENTICAL):
        return "No differences\n"
    line = diff[0]
    idx = diff[1]
    try:
        formt = singleline_diff_format(fn1[line], fn2[line], idx)
    except IndexError:
        if len(fn1) > len(fn2):
            return f"Line {line}:\n{fn1[line]}\n^\n\n"
        elif len(fn2) > len(fn1):
            return f"Line {line}:\n{fn2[line]}\n^\n\n"

    return f"Line {line}:\n{formt}"
