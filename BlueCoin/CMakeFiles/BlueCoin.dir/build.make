# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.19

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Disable VCS-based implicit rules.
% : %,v


# Disable VCS-based implicit rules.
% : RCS/%


# Disable VCS-based implicit rules.
% : RCS/%,v


# Disable VCS-based implicit rules.
% : SCCS/s.%


# Disable VCS-based implicit rules.
% : s.%


.SUFFIXES: .hpux_make_needs_suffix_list


# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/local/bin/cmake

# The command to remove a file.
RM = /usr/local/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/pi/BlueCoin

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/pi/BlueCoin

# Include any dependencies generated for this target.
include CMakeFiles/BlueCoin.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/BlueCoin.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/BlueCoin.dir/flags.make

CMakeFiles/BlueCoin.dir/main.cpp.o: CMakeFiles/BlueCoin.dir/flags.make
CMakeFiles/BlueCoin.dir/main.cpp.o: main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/pi/BlueCoin/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/BlueCoin.dir/main.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/BlueCoin.dir/main.cpp.o -c /home/pi/BlueCoin/main.cpp

CMakeFiles/BlueCoin.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/BlueCoin.dir/main.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/pi/BlueCoin/main.cpp > CMakeFiles/BlueCoin.dir/main.cpp.i

CMakeFiles/BlueCoin.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/BlueCoin.dir/main.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/pi/BlueCoin/main.cpp -o CMakeFiles/BlueCoin.dir/main.cpp.s

CMakeFiles/BlueCoin.dir/BlueCoinController.cpp.o: CMakeFiles/BlueCoin.dir/flags.make
CMakeFiles/BlueCoin.dir/BlueCoinController.cpp.o: BlueCoinController.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/pi/BlueCoin/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/BlueCoin.dir/BlueCoinController.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/BlueCoin.dir/BlueCoinController.cpp.o -c /home/pi/BlueCoin/BlueCoinController.cpp

CMakeFiles/BlueCoin.dir/BlueCoinController.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/BlueCoin.dir/BlueCoinController.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/pi/BlueCoin/BlueCoinController.cpp > CMakeFiles/BlueCoin.dir/BlueCoinController.cpp.i

CMakeFiles/BlueCoin.dir/BlueCoinController.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/BlueCoin.dir/BlueCoinController.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/pi/BlueCoin/BlueCoinController.cpp -o CMakeFiles/BlueCoin.dir/BlueCoinController.cpp.s

CMakeFiles/BlueCoin.dir/Exceptions.cpp.o: CMakeFiles/BlueCoin.dir/flags.make
CMakeFiles/BlueCoin.dir/Exceptions.cpp.o: Exceptions.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/pi/BlueCoin/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object CMakeFiles/BlueCoin.dir/Exceptions.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/BlueCoin.dir/Exceptions.cpp.o -c /home/pi/BlueCoin/Exceptions.cpp

CMakeFiles/BlueCoin.dir/Exceptions.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/BlueCoin.dir/Exceptions.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/pi/BlueCoin/Exceptions.cpp > CMakeFiles/BlueCoin.dir/Exceptions.cpp.i

CMakeFiles/BlueCoin.dir/Exceptions.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/BlueCoin.dir/Exceptions.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/pi/BlueCoin/Exceptions.cpp -o CMakeFiles/BlueCoin.dir/Exceptions.cpp.s

# Object files for target BlueCoin
BlueCoin_OBJECTS = \
"CMakeFiles/BlueCoin.dir/main.cpp.o" \
"CMakeFiles/BlueCoin.dir/BlueCoinController.cpp.o" \
"CMakeFiles/BlueCoin.dir/Exceptions.cpp.o"

# External object files for target BlueCoin
BlueCoin_EXTERNAL_OBJECTS =

BlueCoin: CMakeFiles/BlueCoin.dir/main.cpp.o
BlueCoin: CMakeFiles/BlueCoin.dir/BlueCoinController.cpp.o
BlueCoin: CMakeFiles/BlueCoin.dir/Exceptions.cpp.o
BlueCoin: CMakeFiles/BlueCoin.dir/build.make
BlueCoin: ASTSerialLib/libASTSerialLib.a
BlueCoin: AudioSerialLib/libAudioSerialLib.a
BlueCoin: CMakeFiles/BlueCoin.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/pi/BlueCoin/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Linking CXX executable BlueCoin"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/BlueCoin.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/BlueCoin.dir/build: BlueCoin

.PHONY : CMakeFiles/BlueCoin.dir/build

CMakeFiles/BlueCoin.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/BlueCoin.dir/cmake_clean.cmake
.PHONY : CMakeFiles/BlueCoin.dir/clean

CMakeFiles/BlueCoin.dir/depend:
	cd /home/pi/BlueCoin && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/pi/BlueCoin /home/pi/BlueCoin /home/pi/BlueCoin /home/pi/BlueCoin /home/pi/BlueCoin/CMakeFiles/BlueCoin.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/BlueCoin.dir/depend
