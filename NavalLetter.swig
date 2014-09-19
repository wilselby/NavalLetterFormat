/* NavalLetter.swig */

%module NavalLetter

%{
	#include <time.h>
	#include <string>
	#include <cctype>
	#include <stdio.h>
	#include <algorithm>
	#include <vector>
	#include <iostream>
	#include "/home/ubuntu/DocxFactory/include/WordProcessingCompiler.h"
	#include "/home/ubuntu/DocxFactory/include/WordProcessingMerger.h"

	extern DocxFactory::WordProcessingMerger& initialize(void);
	extern void print_Reply(DocxFactory::WordProcessingMerger& l_mergerIn, std::string user_SSIC, std::string user_code_serial, std::string user_date);
	extern void save_Output(DocxFactory::WordProcessingMerger& l_mergerIn, std::string user_fileName);
	extern void print_Header(DocxFactory::WordProcessingMerger& l_mergerIn, std::string user_unit, std::string user_address, std::string user_address2);
	extern void print_FromToSubj(DocxFactory::WordProcessingMerger& l_mergerIn, std::string user_from, std::string user_to, std::string user_subj);
	extern void print_Via(DocxFactory::WordProcessingMerger& l_mergerIn, std::vector<std::string> user_via);
	extern void print_Ref(DocxFactory::WordProcessingMerger& l_mergerIn, std::vector<std::string> user_ref);
	extern void print_Encl(DocxFactory::WordProcessingMerger& l_mergerIn, std::vector<std::string> user_encl);

	extern void print_Body(DocxFactory::WordProcessingMerger& l_mergerIn, std::vector<std::string> user_bodyLvl, std::vector<std::string> user_body);

	extern void print_Copy(DocxFactory::WordProcessingMerger& l_mergerIn, std::vector<std::string> user_copy);

	extern void print_Sig(DocxFactory::WordProcessingMerger& l_mergerIn, std::string user_sig);

 %}

%include std_vector.i
%include std_string.i
using std::string;

%include "/home/ubuntu/DocxFactory/include/WordProcessingCompiler.h"
%include "/home/ubuntu/DocxFactory/include/WordProcessingMerger.h"
using namespace DocxFactory;

%apply char * {std::string &x};

namespace std {
   %template(StringVector) vector<string>;
}

/* Variables */


/* Functions */
extern DocxFactory::WordProcessingMerger& initialize(void);

extern void print_Reply(DocxFactory::WordProcessingMerger& l_mergerIn, std::string user_SSIC, std::string user_code_serial, std::string user_date);

extern void print_Header(DocxFactory::WordProcessingMerger& l_mergerIn, std::string user_unit, std::string user_address, std::string user_address2);

extern void print_FromToSubj(DocxFactory::WordProcessingMerger& l_mergerIn, std::string user_from, std::string user_to, std::string user_subj);

extern void print_Via(DocxFactory::WordProcessingMerger& l_mergerIn, std::vector<std::string> user_via);
extern void print_Ref(DocxFactory::WordProcessingMerger& l_mergerIn, std::vector<std::string> user_ref);
extern void print_Encl(DocxFactory::WordProcessingMerger& l_mergerIn, std::vector<std::string> user_encl);

extern void print_Body(DocxFactory::WordProcessingMerger& l_mergerIn, std::vector<std::string> user_bodyLvl, std::vector<std::string> user_body);

extern void print_Copy(DocxFactory::WordProcessingMerger& l_mergerIn, std::vector<std::string> user_copy);

extern void print_Sig(DocxFactory::WordProcessingMerger& l_mergerIn, std::string user_sig);

extern void save_Output(DocxFactory::WordProcessingMerger& l_mergerIn, std::string user_fileName);








