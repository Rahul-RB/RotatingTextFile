# Rotating Text File
A rotating file handler which rotates when YOU want it to, rather than based on bytes size. 

### When to use this module?
- When you have that niche case of logs being written into some text file from several functions and you just want it to rotate without having to re-write all the write calls with some new package.

### Why not use RotatingFileHandler provided by Python's logging module?
- If you are thinking of logging, please use RotatingFileHandler. It provides doRollover method which does the same functionality but with all the logging APIs.
- This module aims to solve cases of code where outputs were just being dumped into some file and over time the code grew so big that rotating the text file was needed without distrubing/refactoring the entire codebase.

### Installation
`pip install RotatingTextFile`

### Usage:
- Any existing code with text file can be replaced with the RotateTextFile constructor and a checker function.
- Eg:

If you have some code like:
```
with open("path/to/text/file","w") as fp:
  fp.write("some log")
```
All you have to do is:
```
def condition():
  return some_variable==0

with RotateTextFile("path/to/text/file",condition,10) as fp: #10 is backupCount as in RotatingFileHandler
  fp.write("some log")
``` 

- `condition` is called on every write. You can think of it as an analogy to a sort function which takes your `checking` function as an input.
- `RotateTextFile` inherits `io.TextIOWrapper`, so to pass any arguments specific to `io.TextIOWrapper`'s constructor, just pass them as Keyword Arguments.
- Since a file is rotated only on write, `RotateTextFile` constructor opens the file in `ab+` mode. Other supported modes are :`wb`. `mode` can be passed as:
`RotateTextFile("path/to/text/file",condition,10,'wb'):`
- `backupCount` indicates how many backups a file can have before it is rotated.
- Like `RotatingFileHandler` provided by Python's logging module, `RotateTextFile` guarentees that the file being written to will ALWAYS be `filename.log`
