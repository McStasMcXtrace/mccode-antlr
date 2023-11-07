
//////////////////////////////////////////////////////////////////////////////
//OpenCL lilbrary file for McStas
//
// global variables assigned to the OpenCL mechanism
// only initialised once
//Created by Jinyan LIU
//Date july 2014
//////////////////////////////////////////////////////////////////////////////



#ifdef USE_OPENCL
#ifndef OPENCL_LIB_H
#define OPENCL_LIB_H

#include <>

// this structure holds the full GPU context initialised from a Kernel source file
// to get if use: s = oclInitKernel(filename, 1);
#define MAX_GPU_COUNT 8

struct opencl_context {
  cl_context       GPUContext;                     // OpenCL context
  cl_command_queue CommandQueue[MAX_GPU_COUNT];      // OpenCL command queue
  cl_kernel        Kernel;
};

struct opencl_context oclInitKernel(char *filename, cl_uint nDevice);

// Mersenne OCL implementation
#define   MT_RNG_COUNT 4096
#define          MT_MM 397            
#define          MT_NN 624               
#define       MT_WMASK 0xFFFFFFFFU
#define       MT_UMASK 0x80000000U      
#define       MT_LMASK 0x7fffffffU       
#define      MT_SHIFT0 12
#define      MT_SHIFTB 7
#define      MT_SHIFTC 15
#define      MT_SHIFT1 18
#define      DCMT_SEED 4172

////////////////////////////////////////////////////////////////////////////////
//OpenCL Global Variable 
//////////////////////////////////////////////////////////////////////////////// 
struct opencl_context oclContext_mt;
unsigned int        **oclContext_mt_buffer=NULL;      // buffer holding a list of random numbers, on the CPU
cl_mem               *oclContext_mt_buffer_GPU=NULL;  // buffer holding a list of random numbers, on the GPU/OpenCL
int                   oclContext_mt_counter = -2;     // index of random number read from buffer

void         mt_srandom_opencl(unsigned long s);
unsigned int mt_random_opencl(void);

#endif
#endif
