/*
 *  NavalLetter.cpp
 *  Naval Letter Format
 *
 *  Created by Wil Selby on 7/4/14.
 *
 */

/* TODO:
 *
 *
 *
 *
 */

/* Includes */
#include <time.h>
#include <string>
#include <stdio.h>
#include <cctype>
#include <algorithm>
#include <vector>
#include <iostream>
#include "/home/ubuntu/DocxFactory/include/WordProcessingCompiler.h"
#include "/home/ubuntu/DocxFactory/include/WordProcessingMerger.h"
#include <sstream>

using namespace DocxFactory;
using namespace std;

/* Variables */
char alphabet[26] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};


/* Functions */

std::string convertInt(int number)
{
    stringstream ss;//create a stringstream
    ss << number;//add number to the stream
    return ss.str();//return a string with the contents of the stream
}

DocxFactory::WordProcessingMerger& initialize(void){

		//Initiate Compiler
		WordProcessingCompiler& l_compiler = WordProcessingCompiler::getInstance();
        
		//Initiate Merger
		WordProcessingMerger& l_merger = WordProcessingMerger::getInstance();
        
		//Compile DFW file (if it needs to be updated)
		//l_compiler.compile("/home/wilselby/Dropbox/DocX/Final/NavalLetterTemplate.docx","/home/wilselby/Dropbox/DocX/Final/NavalLetterTemplate.dfw");
        
		//Load DFW file
		l_merger.load("/home/ubuntu/NavalLetterFormat/NavalLetterTemplate.dfw");

	return l_merger;

	printf("Initialized \n");

}


void print_Header(DocxFactory::WordProcessingMerger& l_mergerIn, std::string user_unit, std::string user_address, std::string user_address2){

        l_mergerIn.setClipboardValue("_header", "Unit_header", user_unit);
        l_mergerIn.setClipboardValue("_header", "Unit_address", user_address);
        l_mergerIn.setClipboardValue("_header", "Unit_address2", user_address2);

	printf("Printed Header Block \n");

}

void print_Reply(DocxFactory::WordProcessingMerger& l_mergerIn, std::string user_SSIC, std::string user_code_serial, std::string user_date){

	l_mergerIn.setClipboardValue("ReplySSIC", "SSIC", user_SSIC );
	l_mergerIn.paste("ReplySSIC");

	l_mergerIn.setClipboardValue("ReplyCode", "Code_in", user_code_serial);
	l_mergerIn.paste("ReplyCode");
        
	l_mergerIn.setClipboardValue("ReplyDate", "Date_in", user_date);
	l_mergerIn.paste("ReplyDate");

	printf("Printed Reply Block \n");

}


void print_FromToSubj(DocxFactory::WordProcessingMerger& l_mergerIn, std::string user_from, std::string user_to, std::string user_subj){

	l_mergerIn.setClipboardValue("FromLine", "FromField", user_from );
	l_mergerIn.paste("FromLine");
        
	l_mergerIn.setClipboardValue("ToLine", "ToField", user_to );
	l_mergerIn.paste("ToLine");
        
        // Make sure it is all caps
        std::string subjIn( user_subj );
        std::transform( subjIn.begin(), subjIn.end(), subjIn.begin(),std::ptr_fun <int, int> ( std::toupper));
	l_mergerIn.setClipboardValue("Subject", "Subj_in", subjIn );
	l_mergerIn.paste("Subject");
        l_mergerIn.setClipboardValue("_header", "Subj_in", subjIn );

	printf("Printed From/To/Subj Block \n");

}

void print_Via(DocxFactory::WordProcessingMerger& l_mergerIn, std::vector<std::string> user_via){
    
	std::string s;

	//Print first Via                            
        l_mergerIn.setClipboardValue("Via1", "Via_in", user_via[0]);
        l_mergerIn.paste("Via1");
        
	//Print additional Vias                   
 	for (unsigned int i=1; i < user_via.size(); i++){
        	s = convertInt(i+1);	//start at #2
                l_mergerIn.setClipboardValue("Via2", "via_num_in", s);
                l_mergerIn.setClipboardValue("Via2", "Via_in2", user_via[i]);
                l_mergerIn.paste("Via2");
		//cout << user_via[i] << endl;	//testing code
        }

	printf("Printed Via Block \n");

}

void print_Ref(DocxFactory::WordProcessingMerger& l_mergerIn, std::vector<std::string> user_ref){
    
	//Print first Ref
	l_mergerIn.setClipboardValue("Reference1", "Ref_in", user_ref[0]);
        l_mergerIn.paste("Reference1");
                            
           
	//Print additional Vias                   
 	for (unsigned int i=1; i < user_ref.size(); i++){

		std::string alph(&alphabet[i],1);	//start at b
                l_mergerIn.setClipboardValue("Reference2", "ref_alph_in", alph);
                l_mergerIn.setClipboardValue("Reference2", "Ref_in2", user_ref[i]);
                l_mergerIn.paste("Reference2");
                //cout << user_ref[i] << endl;	//testing code
        }

	printf("Printed Ref Block \n");   
   
}
void print_Encl(DocxFactory::WordProcessingMerger& l_mergerIn, std::vector<std::string> user_encl){

	std::string s;

	//Print first Encl
        l_mergerIn.setClipboardValue("Enclosure1", "Encl_in", user_encl[0]);
        l_mergerIn.paste("Enclosure1");
                            
        for (unsigned int i=1; i < user_encl.size(); i++){
                                
		s = convertInt(i+1);	//start at #2
                l_mergerIn.setClipboardValue("Enclosure2", "encl_num_in", s);
                l_mergerIn.setClipboardValue("Enclosure2", "Encl_in2", user_encl[i]);
                l_mergerIn.paste("Enclosure2");
		//cout << user_encl[i] << endl;	//testing code
        }

	printf("Printed Encl Block \n");  
}

void print_Body(DocxFactory::WordProcessingMerger& l_mergerIn, std::vector<std::string> user_bodyLvl, std::vector<std::string> user_body){

	std::string s;
	int counter_lvl_1 = 0;
    	int counter_lvl_2 = 0;
    	int counter_lvl_3 = 0;

	for (unsigned int i=0; i < user_bodyLvl.size(); i++){

		if(user_bodyLvl[i] == "1"){
			
			counter_lvl_1++;
        		s = convertInt(counter_lvl_1);
        		l_mergerIn.setClipboardValue("bodylvl1", "bodynum1", s);
        		l_mergerIn.setClipboardValue("bodylvl1", "lvl1_body_in", user_body[i]);
        		l_mergerIn.paste("bodylvl1");
			printf("Level 1: ");
			//cout << user_body[i] << endl;	//testing code
		}

		if(user_bodyLvl[i] == "2"){
			
			if (counter_lvl_2 >= 0) {
        			std::string alph_body(&alphabet[counter_lvl_2],1);
        			l_mergerIn.setClipboardValue("bodylvl2", "bodyalph2", alph_body);
       			}

        		l_mergerIn.setClipboardValue("bodylvl2", "lvl2_body_in", user_body[i]);
        		l_mergerIn.paste("bodylvl2");
        		counter_lvl_2++;
			printf("Level 2: ");
			//cout << user_body[i] << endl;	//testing code
		}

		if(user_bodyLvl[i] == "3"){
			
			counter_lvl_3++;
        		s = convertInt(counter_lvl_3);
        		l_mergerIn.setClipboardValue("bodylvl3", "bodynum3", s);
        		l_mergerIn.setClipboardValue("bodylvl3", "lvl3_body_in", user_body[i]);
        		l_mergerIn.paste("bodylvl3");
			printf("Level 3: ");
			//cout << user_body[i] << endl;	//testing code
		}
	}

	printf("Printed Body Block \n"); 
}


void print_Copy(DocxFactory::WordProcessingMerger& l_mergerIn, std::vector<std::string> user_copy){
   
	//Print first addressee
	l_mergerIn.paste("CopyTo");
        l_mergerIn.setClipboardValue("CopyToAddr", "copy_in", user_copy[0] );
        l_mergerIn.paste("CopyToAddr");
        
	for (unsigned int i=1; i < user_copy.size(); i++){
                            
        	l_mergerIn.setClipboardValue("CopyToAddr", "copy_in", user_copy[i] );
        	l_mergerIn.paste("CopyToAddr");
  		//cout << user_copy[i] << endl;	//testing code
        }

	printf("Printed Copy Block \n"); 
}

void print_Sig(DocxFactory::WordProcessingMerger& l_mergerIn, std::string user_sig){
        
	//Make all CAPS
        std::string sigIn( user_sig );
        std::transform( sigIn.begin(), sigIn.end(), sigIn.begin(),std::ptr_fun <int, int> ( std::toupper));

	//Print Signature
	l_mergerIn.setClipboardValue("Signature", "sig_in", sigIn );
	l_mergerIn.paste("Signature");
	cout << sigIn << endl;	//testing code

	printf("Printed Sig Block \n");
}

void save_Output(DocxFactory::WordProcessingMerger& l_mergerIn, std::string user_fileName){

        //Save Output File
	std::string filePath = "/home/ubuntu/NavalLetterFormat/static/";
	std::string fileType = ".docx";
	//std::string rand = convertInt(rand());
	std::string fileName = filePath + user_fileName + fileType;
	std::string printName = user_fileName + fileType;


	//l_mergerIn.save("/home/wilselby/Dropbox/DocX/Final/NavalLetterFinal.docx");
	l_mergerIn.save(fileName);
	//cout << fileName << endl;

	printf("Saved %s \n", printName.c_str());

}
































