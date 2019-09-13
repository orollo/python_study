#define DRIVERCALLAPI
#include <stdio.h>
#include <stdint.h>
typedef void*( DRIVERCALLAPI *fn_DRV_COMM_Open )(void*);
typedef void(DRIVERCALLAPI *fn_DRV_COMM_Close)(void*);
typedef int(DRIVERCALLAPI *fn_DRV_COMM_Transfer)(void *, unsigned char *, int);

typedef struct DriverCallbacks_t
{
    fn_DRV_COMM_Open                drvcomm_Open;
    fn_DRV_COMM_Close               drvcomm_Close;
    fn_DRV_COMM_Transfer            drvcomm_Transfer;
} DriverCallbacks;

typedef struct InitDataEntry_t
{
    char iface[64];
    void* handle;
} InitDataEntry;

typedef struct InitDataContainer_t
{
    uint32_t size;
    uint32_t id;
    InitDataEntry* data;
} InitDataContainer;

void* dev_Create( void* args )
{
    printf("%s:%d\n", __FUNCTION__, __LINE__);
    InitDataContainer* container = (InitDataContainer *)args;
    printf("%s:%d, size:%d, id:%d\n", __FUNCTION__, __LINE__,
            container->size, container->id);

    InitDataEntry* entry = (InitDataEntry *)container->data;
    printf("%s:%d iface:%s\n", __FUNCTION__, __LINE__, entry->iface);
}

void ftdi_open(void *a)
{
    printf("%s:%d\n", __FUNCTION__, __LINE__);
}

void ftdi_close(void *a)
{
    printf("%s:%d\n", __FUNCTION__, __LINE__);
}

void ftdi_transfer()
{
    printf("%s:%d\n", __FUNCTION__, __LINE__);
}
