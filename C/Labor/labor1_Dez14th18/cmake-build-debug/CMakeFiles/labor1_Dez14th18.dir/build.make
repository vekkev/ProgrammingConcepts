# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.13

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = "/Users/kevingruber/Library/Application Support/JetBrains/Toolbox/apps/CLion/ch-0/183.4588.63/CLion.app/Contents/bin/cmake/mac/bin/cmake"

# The command to remove a file.
RM = "/Users/kevingruber/Library/Application Support/JetBrains/Toolbox/apps/CLion/ch-0/183.4588.63/CLion.app/Contents/bin/cmake/mac/bin/cmake" -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/kevingruber/Desktop/Coding/ProgrammingConcepts/C/Labor/labor1_Dez14th18

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/kevingruber/Desktop/Coding/ProgrammingConcepts/C/Labor/labor1_Dez14th18/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/labor1_Dez14th18.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/labor1_Dez14th18.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/labor1_Dez14th18.dir/flags.make

CMakeFiles/labor1_Dez14th18.dir/main.c.o: CMakeFiles/labor1_Dez14th18.dir/flags.make
CMakeFiles/labor1_Dez14th18.dir/main.c.o: ../main.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/kevingruber/Desktop/Coding/ProgrammingConcepts/C/Labor/labor1_Dez14th18/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/labor1_Dez14th18.dir/main.c.o"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/labor1_Dez14th18.dir/main.c.o   -c /Users/kevingruber/Desktop/Coding/ProgrammingConcepts/C/Labor/labor1_Dez14th18/main.c

CMakeFiles/labor1_Dez14th18.dir/main.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/labor1_Dez14th18.dir/main.c.i"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/kevingruber/Desktop/Coding/ProgrammingConcepts/C/Labor/labor1_Dez14th18/main.c > CMakeFiles/labor1_Dez14th18.dir/main.c.i

CMakeFiles/labor1_Dez14th18.dir/main.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/labor1_Dez14th18.dir/main.c.s"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/kevingruber/Desktop/Coding/ProgrammingConcepts/C/Labor/labor1_Dez14th18/main.c -o CMakeFiles/labor1_Dez14th18.dir/main.c.s

# Object files for target labor1_Dez14th18
labor1_Dez14th18_OBJECTS = \
"CMakeFiles/labor1_Dez14th18.dir/main.c.o"

# External object files for target labor1_Dez14th18
labor1_Dez14th18_EXTERNAL_OBJECTS =

labor1_Dez14th18: CMakeFiles/labor1_Dez14th18.dir/main.c.o
labor1_Dez14th18: CMakeFiles/labor1_Dez14th18.dir/build.make
labor1_Dez14th18: CMakeFiles/labor1_Dez14th18.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/kevingruber/Desktop/Coding/ProgrammingConcepts/C/Labor/labor1_Dez14th18/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable labor1_Dez14th18"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/labor1_Dez14th18.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/labor1_Dez14th18.dir/build: labor1_Dez14th18

.PHONY : CMakeFiles/labor1_Dez14th18.dir/build

CMakeFiles/labor1_Dez14th18.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/labor1_Dez14th18.dir/cmake_clean.cmake
.PHONY : CMakeFiles/labor1_Dez14th18.dir/clean

CMakeFiles/labor1_Dez14th18.dir/depend:
	cd /Users/kevingruber/Desktop/Coding/ProgrammingConcepts/C/Labor/labor1_Dez14th18/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/kevingruber/Desktop/Coding/ProgrammingConcepts/C/Labor/labor1_Dez14th18 /Users/kevingruber/Desktop/Coding/ProgrammingConcepts/C/Labor/labor1_Dez14th18 /Users/kevingruber/Desktop/Coding/ProgrammingConcepts/C/Labor/labor1_Dez14th18/cmake-build-debug /Users/kevingruber/Desktop/Coding/ProgrammingConcepts/C/Labor/labor1_Dez14th18/cmake-build-debug /Users/kevingruber/Desktop/Coding/ProgrammingConcepts/C/Labor/labor1_Dez14th18/cmake-build-debug/CMakeFiles/labor1_Dez14th18.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/labor1_Dez14th18.dir/depend

