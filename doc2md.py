from win32com import client as wc
import os, time

class Pdf_docx_md(object):

    def load_files(self, path):
        '''
            加载所需文件，返回文件名（All）
        '''
        os.chdir(path)
        dir = os.getcwd()
        files = os.listdir(dir)
        for file in files:
            yield file

    def do_exchange(self, file, file_path, change_path):
        '''
            文件转换（pdf2docx2md）
        '''
        word = wc.Dispatch('Word.Application')
        if file[-4:] == '.pdf':
            # pdf转docx
            doc = word.Documents.Open(file_path + file)
            doc.SaveAs('%s\\%s.docx' % (change_path, 'pdf2docx'), 16)
            doc.Close()
            time.sleep(5)
            command = 'C:/pandoc.exe -s {PATH}\\pdf2docx.docx -o {PATH}\\docx2md.md'
            command = command.format(PATH=change_path)
            os.popen(command, 'r')

    def find_mass(self, change_path):
        '''
            内容解析（业务需求函数）
        '''
        total_path = change_path + '\\docx2md.md'
        # 解析md文件
        str_html = open(total_path, 'rb')
        return str_html

    def main(self, file_path, change_path):

        files = self.load_files(file_path)
        for file in files:
            print('正在转换:',file)
            self.do_exchange(file, file_path, change_path)
            print('转换成功！')
            self.find_mass(change_path)


if __name__ == '__main__':

    pdf_docx_md = Pdf_docx_md()
    file_path = 'C:\\product_name\\data\\'
    change_path = 'C:\\product_name\\pad2docx2md\\'
    pdf_docx_md.main(file_path, change_path)