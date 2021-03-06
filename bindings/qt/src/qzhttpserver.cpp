/*
################################################################################
#  THIS FILE IS 100% GENERATED BY ZPROJECT; DO NOT EDIT EXCEPT EXPERIMENTALLY  #
#  Read the zproject/README.md for information about making permanent changes. #
################################################################################
*/

#include "qczmq.h"

///
//  Copy-construct to return the proper wrapped c types
QZhttpServer::QZhttpServer (zhttp_server_t *self, QObject *qObjParent) : QObject (qObjParent)
{
    this->self = self;
}


///
//  Create a new http server
QZhttpServer::QZhttpServer (QZhttpServerOptions *options, QObject *qObjParent) : QObject (qObjParent)
{
    this->self = zhttp_server_new (options->self);
}

///
//  Destroy an http server
QZhttpServer::~QZhttpServer ()
{
    zhttp_server_destroy (&self);
}

///
//  Return the port the server is listening on.
int QZhttpServer::port ()
{
    int rv = zhttp_server_port (self);
    return rv;
}

///
//  Self test of this class.
void QZhttpServer::test (bool verbose)
{
    zhttp_server_test (verbose);

}
/*
################################################################################
#  THIS FILE IS 100% GENERATED BY ZPROJECT; DO NOT EDIT EXCEPT EXPERIMENTALLY  #
#  Read the zproject/README.md for information about making permanent changes. #
################################################################################
*/
