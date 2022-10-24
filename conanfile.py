import os, sys, subprocess
from conans import ConanFile, CMake, tools

class SatlinkConan(ConanFile):
    name = "test"
    version = "1.0.0"
    license = "blop"
    author = "your mama"
    url = "your papa"
    description = ""
    topics = ("fmt")
    settings = "os", "compiler", "build_type", "arch"    
    generators = "cmake"
    exports_sources = "CMakeLists.txt", "conanfile.py", "main.cpp"

    def requirements(self):
        # fmt (string format lib)
        self.requires("fmt/7.1.3")


    def configure_cmake(self):
        cmake = CMake(self)       
        cmake.configure(source_folder=".")
        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()

    def package(self):
        self.copy("*", src="bin", dst="bin")
