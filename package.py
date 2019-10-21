name = "cppunit"

version = "1.14.0"

authors = [
    "Michael Feathers",
    "Jerome Lacoste"
]

description = \
    """
    CppUnit is the C++ port of the famous JUnit framework for unit testing. Test output is in XML for automatic
    testing and GUI based for supervised tests.
    """

requires = [
    "cmake-3+",
    "gcc-6+"
]

variants = [
    ["platform-linux"]
]

tools = [
    "DllPlugInTester"
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "cppunit-{version}".format(version=str(version))

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    env.PKG_CONFIG_PATH.prepend("{root}/lib/pkgconfig")

    # Helper environment variables.
    env.CPPUNIT_BINARY_PATH.set("{root}/bin")
    env.CPPUNIT_INCLUDE_PATH.set("{root}/include")
    env.CPPUNIT_LIBRARY_PATH.set("{root}/lib")
