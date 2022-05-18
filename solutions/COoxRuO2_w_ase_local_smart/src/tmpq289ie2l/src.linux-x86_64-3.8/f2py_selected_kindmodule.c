/* File: f2py_selected_kindmodule.c
 * This file is auto-generated with f2py (version:1.20.2).
 * f2py is a Fortran to Python Interface Generator (FPIG), Second Edition,
 * written by Pearu Peterson <pearu@cens.ioc.ee>.
 * Generation date: Tue May 17 02:25:28 2022
 * Do not edit this file directly unless you know what you are doing!!!
 */

#ifdef __cplusplus
extern "C" {
#endif

/*********************** See f2py2e/cfuncs.py: includes ***********************/
#include "Python.h"
#include "fortranobject.h"
/*need_includes0*/

/**************** See f2py2e/rules.py: mod_rules['modulebody'] ****************/
static PyObject *f2py_selected_kind_error;
static PyObject *f2py_selected_kind_module;

/*********************** See f2py2e/cfuncs.py: typedefs ***********************/
/*need_typedefs*/

/****************** See f2py2e/cfuncs.py: typedefs_generated ******************/
/*need_typedefs_generated*/

/********************** See f2py2e/cfuncs.py: cppmacros **********************/
#ifdef DEBUGCFUNCS
#define CFUNCSMESS(mess) fprintf(stderr,"debug-capi:"mess);
#define CFUNCSMESSPY(mess,obj) CFUNCSMESS(mess) \
    PyObject_Print((PyObject *)obj,stderr,Py_PRINT_RAW);\
    fprintf(stderr,"\n");
#else
#define CFUNCSMESS(mess)
#define CFUNCSMESSPY(mess,obj)
#endif

#ifndef max
#define max(a,b) ((a > b) ? (a) : (b))
#endif
#ifndef min
#define min(a,b) ((a < b) ? (a) : (b))
#endif
#ifndef MAX
#define MAX(a,b) ((a > b) ? (a) : (b))
#endif
#ifndef MIN
#define MIN(a,b) ((a < b) ? (a) : (b))
#endif

#if defined(PREPEND_FORTRAN)
#if defined(NO_APPEND_FORTRAN)
#if defined(UPPERCASE_FORTRAN)
#define F_FUNC(f,F) _##F
#else
#define F_FUNC(f,F) _##f
#endif
#else
#if defined(UPPERCASE_FORTRAN)
#define F_FUNC(f,F) _##F##_
#else
#define F_FUNC(f,F) _##f##_
#endif
#endif
#else
#if defined(NO_APPEND_FORTRAN)
#if defined(UPPERCASE_FORTRAN)
#define F_FUNC(f,F) F
#else
#define F_FUNC(f,F) f
#endif
#else
#if defined(UPPERCASE_FORTRAN)
#define F_FUNC(f,F) F##_
#else
#define F_FUNC(f,F) f##_
#endif
#endif
#endif
#if defined(UNDERSCORE_G77)
#define F_FUNC_US(f,F) F_FUNC(f##_,F##_)
#else
#define F_FUNC_US(f,F) F_FUNC(f,F)
#endif


/************************ See f2py2e/cfuncs.py: cfuncs ************************/
static int
int_from_pyobj(int* v, PyObject *obj, const char *errmess)
{
    PyObject* tmp = NULL;

    if (PyLong_Check(obj)) {
        *v = Npy__PyLong_AsInt(obj);
        return !(*v == -1 && PyErr_Occurred());
    }

    tmp = PyNumber_Long(obj);
    if (tmp) {
        *v = Npy__PyLong_AsInt(tmp);
        Py_DECREF(tmp);
        return !(*v == -1 && PyErr_Occurred());
    }

    if (PyComplex_Check(obj))
        tmp = PyObject_GetAttrString(obj,"real");
    else if (PyBytes_Check(obj) || PyUnicode_Check(obj))
        /*pass*/;
    else if (PySequence_Check(obj))
        tmp = PySequence_GetItem(obj, 0);
    if (tmp) {
        PyErr_Clear();
        if (int_from_pyobj(v, tmp, errmess)) {
            Py_DECREF(tmp);
            return 1;
        }
        Py_DECREF(tmp);
    }
    {
        PyObject* err = PyErr_Occurred();
        if (err == NULL) {
            err = f2py_selected_kind_error;
        }
        PyErr_SetString(err, errmess);
    }
    return 0;
}


/********************* See f2py2e/cfuncs.py: userincludes *********************/
/*need_userincludes*/

/********************* See f2py2e/capi_rules.py: usercode *********************/


/* See f2py2e/rules.py */
/*eof externroutines*/

/******************** See f2py2e/capi_rules.py: usercode1 ********************/


/******************* See f2py2e/cb_rules.py: buildcallback *******************/
/*need_callbacks*/

/*********************** See f2py2e/rules.py: buildapi ***********************/

/********************************* real_kind *********************************/
static char doc_f2py_rout_f2py_selected_kind_kind_real_kind[] = "\
kind_value = real_kind([p,r])\n\nWrapper for ``real_kind``.\
\n\nOther Parameters\n----------------\n"
"p : input int\n"
"r : input int\n"
"\nReturns\n-------\n"
"kind_value : int";
/*  */
static PyObject *f2py_rout_f2py_selected_kind_kind_real_kind(const PyObject *capi_self,
                           PyObject *capi_args,
                           PyObject *capi_keywds,
                           void (*f2py_func)(int*,int*,int*)) {
    PyObject * volatile capi_buildvalue = NULL;
    volatile int f2py_success = 1;
/*decl*/

  int p = 0;
  PyObject *p_capi = Py_None;
  int r = 0;
  PyObject *r_capi = Py_None;
  int kind_value = 0;
    static char *capi_kwlist[] = {"p","r",NULL};

/*routdebugenter*/
#ifdef F2PY_REPORT_ATEXIT
f2py_start_clock();
#endif
    if (!PyArg_ParseTupleAndKeywords(capi_args,capi_keywds,\
        "|OO:f2py_selected_kind.kind.real_kind",\
        capi_kwlist,&p_capi,&r_capi))
        return NULL;
/*frompyobj*/
  /* Processing variable p */
  if (p_capi != Py_None)
    f2py_success = int_from_pyobj(&p,p_capi,"f2py_selected_kind.kind.real_kind() 1st keyword (p) can't be converted to int");
  if (f2py_success) {
  /* Processing variable r */
  if (r_capi != Py_None)
    f2py_success = int_from_pyobj(&r,r_capi,"f2py_selected_kind.kind.real_kind() 2nd keyword (r) can't be converted to int");
  if (f2py_success) {
  /* Processing variable kind_value */
/*end of frompyobj*/
#ifdef F2PY_REPORT_ATEXIT
f2py_start_call_clock();
#endif
/*callfortranroutine*/
        (*f2py_func)(&p,&r,&kind_value);
if (PyErr_Occurred())
  f2py_success = 0;
#ifdef F2PY_REPORT_ATEXIT
f2py_stop_call_clock();
#endif
/*end of callfortranroutine*/
        if (f2py_success) {
/*pyobjfrom*/
/*end of pyobjfrom*/
        CFUNCSMESS("Building return value.\n");
        capi_buildvalue = Py_BuildValue("i",kind_value);
/*closepyobjfrom*/
/*end of closepyobjfrom*/
        } /*if (f2py_success) after callfortranroutine*/
/*cleanupfrompyobj*/
  /* End of cleaning variable kind_value */
  } /*if (f2py_success) of r*/
  /* End of cleaning variable r */
  } /*if (f2py_success) of p*/
  /* End of cleaning variable p */
/*end of cleanupfrompyobj*/
    if (capi_buildvalue == NULL) {
/*routdebugfailure*/
    } else {
/*routdebugleave*/
    }
    CFUNCSMESS("Freeing memory.\n");
/*freemem*/
#ifdef F2PY_REPORT_ATEXIT
f2py_stop_clock();
#endif
    return capi_buildvalue;
}
/****************************** end of real_kind ******************************/

/********************************** int_kind **********************************/
static char doc_f2py_rout_f2py_selected_kind_kind_int_kind[] = "\
kind_value = int_kind([p,r])\n\nWrapper for ``int_kind``.\
\n\nOther Parameters\n----------------\n"
"p : input int\n"
"r : input int\n"
"\nReturns\n-------\n"
"kind_value : int";
/*  */
static PyObject *f2py_rout_f2py_selected_kind_kind_int_kind(const PyObject *capi_self,
                           PyObject *capi_args,
                           PyObject *capi_keywds,
                           void (*f2py_func)(int*,int*,int*)) {
    PyObject * volatile capi_buildvalue = NULL;
    volatile int f2py_success = 1;
/*decl*/

  int p = 0;
  PyObject *p_capi = Py_None;
  int r = 0;
  PyObject *r_capi = Py_None;
  int kind_value = 0;
    static char *capi_kwlist[] = {"p","r",NULL};

/*routdebugenter*/
#ifdef F2PY_REPORT_ATEXIT
f2py_start_clock();
#endif
    if (!PyArg_ParseTupleAndKeywords(capi_args,capi_keywds,\
        "|OO:f2py_selected_kind.kind.int_kind",\
        capi_kwlist,&p_capi,&r_capi))
        return NULL;
/*frompyobj*/
  /* Processing variable p */
  if (p_capi != Py_None)
    f2py_success = int_from_pyobj(&p,p_capi,"f2py_selected_kind.kind.int_kind() 1st keyword (p) can't be converted to int");
  if (f2py_success) {
  /* Processing variable r */
  if (r_capi != Py_None)
    f2py_success = int_from_pyobj(&r,r_capi,"f2py_selected_kind.kind.int_kind() 2nd keyword (r) can't be converted to int");
  if (f2py_success) {
  /* Processing variable kind_value */
/*end of frompyobj*/
#ifdef F2PY_REPORT_ATEXIT
f2py_start_call_clock();
#endif
/*callfortranroutine*/
        (*f2py_func)(&p,&r,&kind_value);
if (PyErr_Occurred())
  f2py_success = 0;
#ifdef F2PY_REPORT_ATEXIT
f2py_stop_call_clock();
#endif
/*end of callfortranroutine*/
        if (f2py_success) {
/*pyobjfrom*/
/*end of pyobjfrom*/
        CFUNCSMESS("Building return value.\n");
        capi_buildvalue = Py_BuildValue("i",kind_value);
/*closepyobjfrom*/
/*end of closepyobjfrom*/
        } /*if (f2py_success) after callfortranroutine*/
/*cleanupfrompyobj*/
  /* End of cleaning variable kind_value */
  } /*if (f2py_success) of r*/
  /* End of cleaning variable r */
  } /*if (f2py_success) of p*/
  /* End of cleaning variable p */
/*end of cleanupfrompyobj*/
    if (capi_buildvalue == NULL) {
/*routdebugfailure*/
    } else {
/*routdebugleave*/
    }
    CFUNCSMESS("Freeing memory.\n");
/*freemem*/
#ifdef F2PY_REPORT_ATEXIT
f2py_stop_clock();
#endif
    return capi_buildvalue;
}
/****************************** end of int_kind ******************************/
/*eof body*/

/******************* See f2py2e/f90mod_rules.py: buildhooks *******************/

static FortranDataDef f2py_kind_def[] = {
  {"real_kind",-1,{{-1}},0,NULL,(void *)f2py_rout_f2py_selected_kind_kind_real_kind,doc_f2py_rout_f2py_selected_kind_kind_real_kind},
  {"int_kind",-1,{{-1}},0,NULL,(void *)f2py_rout_f2py_selected_kind_kind_int_kind,doc_f2py_rout_f2py_selected_kind_kind_int_kind},
  {NULL}
};

static void f2py_setup_kind(char *real_kind,char *int_kind) {
  int i_f2py=0;
  f2py_kind_def[i_f2py++].data = real_kind;
  f2py_kind_def[i_f2py++].data = int_kind;
}
extern void F_FUNC(f2pyinitkind,F2PYINITKIND)(void (*)(char *,char *));
static void f2py_init_kind(void) {
  F_FUNC(f2pyinitkind,F2PYINITKIND)(f2py_setup_kind);
}

/*need_f90modhooks*/

/************** See f2py2e/rules.py: module_rules['modulebody'] **************/

/******************* See f2py2e/common_rules.py: buildhooks *******************/

/*need_commonhooks*/

/**************************** See f2py2e/rules.py ****************************/

static FortranDataDef f2py_routine_defs[] = {

/*eof routine_defs*/
  {NULL}
};

static PyMethodDef f2py_module_methods[] = {

  {NULL,NULL}
};

static struct PyModuleDef moduledef = {
  PyModuleDef_HEAD_INIT,
  "f2py_selected_kind",
  NULL,
  -1,
  f2py_module_methods,
  NULL,
  NULL,
  NULL,
  NULL
};

PyMODINIT_FUNC PyInit_f2py_selected_kind(void) {
  int i;
  PyObject *m,*d, *s, *tmp;
  m = f2py_selected_kind_module = PyModule_Create(&moduledef);
  Py_SET_TYPE(&PyFortran_Type, &PyType_Type);
  import_array();
  if (PyErr_Occurred())
    {PyErr_SetString(PyExc_ImportError, "can't initialize module f2py_selected_kind (failed to import numpy)"); return m;}
  d = PyModule_GetDict(m);
  s = PyUnicode_FromString("1.20.2");
  PyDict_SetItemString(d, "__version__", s);
  Py_DECREF(s);
  s = PyUnicode_FromString(
    "This module 'f2py_selected_kind' is auto-generated with f2py (version:1.20.2).\nFunctions:\n"
"Fortran 90/95 modules:\n""  kind --- real_kind(),int_kind()"".");
  PyDict_SetItemString(d, "__doc__", s);
  Py_DECREF(s);
  s = PyUnicode_FromString("1.20.2");
  PyDict_SetItemString(d, "__f2py_numpy_version__", s);
  Py_DECREF(s);
  f2py_selected_kind_error = PyErr_NewException ("f2py_selected_kind.error", NULL, NULL);
  /*
   * Store the error object inside the dict, so that it could get deallocated.
   * (in practice, this is a module, so it likely will not and cannot.)
   */
  PyDict_SetItemString(d, "_f2py_selected_kind_error", f2py_selected_kind_error);
  Py_DECREF(f2py_selected_kind_error);
  for(i=0;f2py_routine_defs[i].name!=NULL;i++) {
    tmp = PyFortranObject_NewAsAttr(&f2py_routine_defs[i]);
    PyDict_SetItemString(d, f2py_routine_defs[i].name, tmp);
    Py_DECREF(tmp);
  }


/*eof initf2pywraphooks*/
  PyDict_SetItemString(d, "kind", PyFortranObject_New(f2py_kind_def,f2py_init_kind));
/*eof initf90modhooks*/

/*eof initcommonhooks*/


#ifdef F2PY_REPORT_ATEXIT
  if (! PyErr_Occurred())
    on_exit(f2py_report_on_exit,(void*)"f2py_selected_kind");
#endif
  return m;
}
#ifdef __cplusplus
}
#endif
