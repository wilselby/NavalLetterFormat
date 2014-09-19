import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

import NavalLetter


from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('naval_letter.html')

class FormPageHandler(tornado.web.RequestHandler):
    def post(self):

	#Initialize DocX
	l_MergerIn = NavalLetter.initialize()

	#Header Information
	user_unit = "2D BATTALION, 9TH MARINES"
        user_address = "PSC BOX 20136"
        user_address2 = "CAMP LEJEUNE, NORTH CAROLINA 28542-0136"

	NavalLetter.print_Header(l_MergerIn, str(user_unit), str(user_address), str(user_address2))

	#Reply Block
        user_SSIC = self.get_argument('SSIC')
        user_code_serial = self.get_argument('ReplyCode')
        user_date = self.get_argument('Date')

	NavalLetter.print_Reply(l_MergerIn, str(user_SSIC), str(user_code_serial), str(user_date))

	#From/To/Subj Block
        user_from = self.get_argument('From')
        user_to = self.get_argument('To')
        user_subj = self.get_argument('Subj')

	NavalLetter.print_FromToSubj(l_MergerIn, str(user_from), str(user_to), str(user_subj))

	#Optional Blocks
	ifVia = self.get_argument('ifVia')
	if ifVia == 'yes':
		user_via = self.request.arguments.get("ViaTextBox") 
		NavalLetter.print_Via(l_MergerIn, user_via)	

	ifRef = self.get_argument('ifRef')
	if ifRef == 'yes':
		user_ref = self.request.arguments.get("RefTextBox") 
		NavalLetter.print_Ref(l_MergerIn, user_ref)
	
	ifEncl = self.get_argument('ifEncl')
	if ifEncl == 'yes':
		user_encl = self.request.arguments.get("EnclTextBox") 
		NavalLetter.print_Encl(l_MergerIn, user_encl)

	#Body
	bodyLvl = self.request.arguments.get("BodyLevel")
	user_body = self.request.arguments.get("BodyBlocks")
	NavalLetter.print_Body(l_MergerIn, bodyLvl, user_body);

	#Signature
	user_sig = self.get_argument('Sig')
	NavalLetter.print_Sig(l_MergerIn, str(user_sig))

	#Copy To
	ifCopy = self.get_argument('ifCopy')
	if ifCopy == 'yes':
		user_copy = self.request.arguments.get("CopyTextBox") 
		NavalLetter.print_Copy(l_MergerIn, user_copy)

	print self.request.arguments	#print out all variables in the form

	#Save output
	user_fileName = self.get_argument('Filename')
	NavalLetter.save_Output(l_MergerIn, str(user_fileName))
	fileName = "/home/ubuntu/NavalLetterFormat/static/" + user_fileName + ".docx"
	fullFile = user_fileName + ".docx"
	#print fileName

	#Display output
	self.render('download.html',filename = fullFile)
        #self.render('poem.html', roads=str(user_date), wood=str(user_SSIC), made=str(user_date), difference=str(user_code_serial))

class DownloadPageHandler(tornado.web.RequestHandler):
    def get(self):
	self.render('download.html')

    #	file_name = "/home/wilselby/Dropbox/DocX/Final/static/" + "NavalLetterFinal2.docx"
    #	buf_size = 4096
    #	self.set_header('Content-Type', 'application/octet-stream')
    #	self.set_header('Content-Disposition', 'attachment; filename=' + file_name)
    #	with open(file_name, 'r') as f:
     #       while True:
      #      	data = f.read(buf_size)
       #     	if not data:
        #            break
         #   	self.write(data)
     	#self.finish()

#Main
if __name__ == '__main__':
    tornado.options.parse_command_line()
    handlers=[(r'/', IndexHandler),
              (r'/NLFform', FormPageHandler), 
              (r'/download', DownloadPageHandler)]
    settings = {'debug': True, 
               'template_path':os.path.join(os.path.dirname(__file__), "templates"),       		       'static_path':os.path.join(os.path.dirname(__file__), "static") }
    app = tornado.web.Application(handlers, **settings )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


    
