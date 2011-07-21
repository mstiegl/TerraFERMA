
#ifndef __DIAGNOSTICS_FILE_H
#define __DIAGNOSTICS_FILE_H

#include <cstdio>
#include <fstream>
#include <string>
#include "StatFile.h"
#include "Bucket.h"

namespace buckettools
{

  class DiagnosticsFile : public StatFile
  {
  public:
    
    DiagnosticsFile(const std::string name);
 
    ~DiagnosticsFile();
    
    void write_header(const Bucket &bucket, 
                      const bool &timestepping);

  private:

    void header_bucket_(const Bucket &bucket,
                        uint &column);

    void header_functionbucket_(FunctionBucket_const_it f_begin, 
                                FunctionBucket_const_it f_end, 
                                uint &column);
  };
  
}
#endif
