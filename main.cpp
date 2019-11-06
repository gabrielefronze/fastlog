//
// Created by Gabriele Gaetano Fronzé on 2019-11-06.
//

#include "logf.h"

using namespace logf;

int main(){
  std::cout << "Showing effect of various loglevels:";

  std::cout << "\n\nLOGLEVEL = DEBUG\n";

  logLevel = DEBUG;

  logf(INFO, "Info");
  logf(DEBUG, "Debug");
  logf(ERROR, "Error");

  std::cout << "\n\nLOGLEVEL = INFO\n";

  logLevel = INFO;

  logf(INFO, "Info");
  logf(DEBUG, "Debug");
  logf(ERROR, "Error");

  std::cout << "\n\nLOGLEVEL = ERROR\n";

  logLevel = ERROR;

  logf(INFO, "Info");
  logf(DEBUG, "Debug");
  logf(ERROR, "Error");

  std::cout << "\n\nLOGLEVEL = SILENT\n";

  logLevel = SILENT;

  logf(INFO, "Info");
  logf(DEBUG, "Debug");
  logf(ERROR, "Error");

  return 0;
}