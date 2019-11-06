//
// Created by Gabriele Gaetano Fronzé on 2019-11-06.
//

#include "fastlog.h"

using namespace fastlog;

int main(){
  std::cout << "Showing effect of various loglevels:";

  std::cout << "\n\nLOGLEVEL = DEBUG\n";

  logLevel = DEBUG;

  fastlog(INFO, "Info");
  fastlog(DEBUG, "Debug");
  fastlog(ERROR, "Error");

  std::cout << "\n\nLOGLEVEL = INFO\n";

  logLevel = INFO;

  fastlog(INFO, "Info");
  fastlog(DEBUG, "Debug");
  fastlog(ERROR, "Error");

  std::cout << "\n\nLOGLEVEL = ERROR\n";

  logLevel = ERROR;

  fastlog(INFO, "Info");
  fastlog(DEBUG, "Debug");
  fastlog(ERROR, "Error");

  std::cout << "\n\nLOGLEVEL = SILENT\n";

  logLevel = SILENT;

  fastlog(INFO, "Info");
  fastlog(DEBUG, "Debug");
  fastlog(ERROR, "Error");

  return 0;
}