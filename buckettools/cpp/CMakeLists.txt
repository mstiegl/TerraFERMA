# The project name for buckettools (sets up environment variables for binary and source directories)
project(buckettools_cpp)

# Write a template header file to disk at configuration time
# (this holds the template for the mercurial id information that will
#  be replaced at build time by a suitable variable - using the script
#  below)
file(
    WRITE ${PROJECT_BINARY_DIR}/builddefs.h.in
    "#define __HG_ID__ \"@HG_ID@\"\n"
    )

# Write a cmake script to disk at configuration time
# (this will run hg - at compile time - and record the id info
#  to an environment variable which can be used to write a
#  header file for the build)
file(
    WRITE ${PROJECT_BINARY_DIR}/builddefs.cmake
    "find_program(HAVE_HG hg)
    if(HAVE_HG)
        execute_process (
           COMMAND hg id -i 
           WORKING_DIRECTORY \${DIR}
           OUTPUT_VARIABLE HG_ID
           ERROR_VARIABLE HG_ERR
           OUTPUT_STRIP_TRAILING_WHITESPACE
           ERROR_STRIP_TRAILING_WHITESPACE
           )
        if(HG_ERR)
           set(HG_ID "hg_id_not_found")
        endif(HG_ERR)
    else(HAVE_HG)
        set(HG_ID "hg_not_found")
    endif(HAVE_HG)
    configure_file(\${SRC} \${DST} @ONLY)
    "
    )

# add a target that runs the above cmake script and creates the header
# file containing the hg id information
add_custom_target(
    builddefs
    ${CMAKE_COMMAND} -D SRC="${PROJECT_BINARY_DIR}/builddefs.h.in"
                     -D DST="${PROJECT_BINARY_DIR}/builddefs.h"
                     -D DIR="${PROJECT_SOURCE_DIR}/../../"
                     -P "${PROJECT_BINARY_DIR}/builddefs.cmake"
    )


# include the buckettools include directory and the binary directory (for builddefs and the systemswrapper)
include_directories("${PROJECT_SOURCE_DIR}/../include" ${PROJECT_BINARY_DIR})
# include python
include_directories(${PYTHON_INCLUDE_PATH})
# generate a library - really the main point of this whole process
add_library(buckettools_cpp Bucket.cpp SpudBucket.cpp SystemBucket.cpp SpudSystemBucket.cpp
                            FunctionBucket.cpp SpudFunctionBucket.cpp
                            SolverBucket.cpp SpudSolverBucket.cpp 
                            SpudBase.cpp PythonExpression.cpp PythonInstance.cpp
                            InitialConditionExpression.cpp
                            GenericDetectors.cpp PointDetectors.cpp PythonDetectors.cpp
                            StatFile.cpp DiagnosticsFile.cpp
                            BucketPETScBase.cpp BucketDolfinBase.cpp)
# tell cmake that this file doesn't exist until build time
set_source_files_properties(builddefs.h PROPERTIES GENERATED 1)
# the project depends on this target
add_dependencies(buckettools_cpp builddefs)
# link to python
target_link_libraries(buckettools_cpp ${PYTHON_LIBRARIES})

