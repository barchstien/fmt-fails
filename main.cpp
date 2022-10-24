#include <iostream>
#include <fmt/core.h>

int main(int argc, char* argv[])
{
    std::cout << "hello from cout" << std::endl;
    fmt::print("Don't {}\n", "panic");
    return 0;
}
