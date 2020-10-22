//
// Created by Gabriele Gaetano Fronzé on 2019-11-06.
//

#ifndef LOGF_FASTLOG_H
#define LOGF_FASTLOG_H

#include <iostream>
#include <array>
#include <string>

namespace fastlog {
  enum Level {
    SILENT = 0,
    ERROR = 1,
    INFO = 2,
    DEBUG = 3
  } typedef Level;

  extern Level logLevel;

  static const std::array<std::string, 4> Colors
          {
                  "",
                  "\x1B[1;31m[ERROR]\t", // ERROR: Bold Red
                  "\x1B[1;34m[INFO]\t", // INFO: Bold Blue
                  "\x1B[1;33m[DEBUG]\t"  // DEBUG: Green
          };

  static void fastlog_internal(const Level level, const std::string s) {
    std::FILE *output = (level == Level::ERROR ? stderr : stdout);
    if (level <= logLevel) {
      std::fprintf(output, "%s", Colors[level].data());
      std::fprintf(output, "%s", s.data());
      std::fprintf(output, "\x1B[0m");
      std::fprintf(output, "\n");
    }
  }

  template<typename... Args>
  void fastlog_internal(const Level level, const std::string s, Args... args) {
    std::FILE *output = (level == Level::ERROR ? stderr : stdout);
    if (level <= logLevel) {
      std::fprintf(output, "%s", Colors[level].data());
      std::fprintf(output, s.data(), args...);
      std::fprintf(output, "\x1B[0m");
      std::fprintf(output, "\n");
    }
  }
}

#define fastlog(lvl, msg, ...) { fastlog_internal(lvl, "" msg, ##__VA_ARGS__); } (void)0

#endif //LOGF_FASTLOG_H
