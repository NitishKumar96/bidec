'use babel';
/*jshint esversion: 6 */
import CommentsView from './comments-view';
import { CompositeDisposable } from 'atom';

export default {

  commentsView: null,
  modalPanel: null,
  subscriptions: null,

  activate(state) {
    this.commentsView = new CommentsView(state.commentsViewState);
    this.modalPanel = atom.workspace.addModalPanel({
      item: this.commentsView.getElement(),
      visible: false
    });

    // Events subscribed to in atom's system can be easily cleaned up with a CompositeDisposable
    this.subscriptions = new CompositeDisposable();

    // Register command that toggles this view
    this.subscriptions.add(atom.commands.add('atom-workspace', {
      'comments:toggle': () => this.toggle(),
      'comments:checkLine': () => this.checkLine(),
      'comments:print_comment':()=> this.print_comment(),
    }));
  },

  deactivate() {
    this.modalPanel.destroy();
    this.subscriptions.dispose();
    this.commentsView.destroy();
  },

  serialize() {
    return {
      commentsViewState: this.commentsView.serialize()
    };
  },

  toggle()
  {
    let editor=atom.workspace.getActiveTextEditor();
    if (editor)
    {
    let selection = editor.getSelectedText();
    let reversed = selection.split('').reverse().join('');
    // editor.insertText(reversed);
    editor.insertText("\n my name is Nitish");
    }
  },

  print_comment()
    {

    },


  checkLine()
    {
        let Texteditor=atom.workspace.getActiveTextEditor();

        if (Texteditor)
        {
          if (Texteditor.getTitle().split(".")[1]=="js")
            {
                // take the current cursor by the buffer
                var cursor_position = Texteditor.getCursorBufferPosition();
                // make object for the current buffer
                var buffer = Texteditor.getBuffer();
                // take the line number from the cursore position point
                var lineNo= cursor_position.row;
                // store the current line into the string
                let text = Texteditor.lineTextForBufferRow(cursor_position.row);

                // check whether the line has the function keyeord or not
                // if function is present
                if (/\bfunction\b/.test(text))
                {
                    // analyze the data from the current line
                    var string_data = text.trim().split(" ");

                    // revore the text from the current line
                    buffer.deleteRow(cursor_position.row);

                    // add the comment block for the function
                    Texteditor.insertText("\n/*** Function *** \n");
                    // print the function name
                    let function_name=string_data[string_data.indexOf("function")+1];
                    function_name= function_name.split("(")[0];
                    Texteditor.insertText("* Name:  "+function_name+"\n");
                    // print obj taken by the function
                    let startb= text.indexOf("(");
                    let endb=text.indexOf(")");
                    var i, obj="";
                    for (i=startb+1; i< endb;i+=1){
                      obj= obj+ text[i];
                    }
                    let obj_str=obj.split(",");
                    Texteditor.insertText("* Parameters:  \n");
                    for (i=0;i<obj_str.length;i+=1){
                      Texteditor.insertText("* \t\t\t\t=> "+obj_str[i]+"\n");
                    }
                    Texteditor.insertText("* Returns: ");
                    Texteditor.insertText("\n***/\n");

                    // rewrite the function line in a proper way
                    let declaration="function"+" "+function_name+"("+String(obj_str)+")";
                    Texteditor.insertText(declaration+"\n");
                    cursor_position = Texteditor.getCursorBufferPosition();
                    Texteditor.insertText("{\n\n\n}");
                    cursor_position.row+=1;
                    Texteditor.setCursorBufferPosition(cursor_position);
                    Texteditor.insertText("\t");

                }



              }

              Texteditor.insertText("\n"); // if it is not js file or not fn

        }

        else{
          Texteditor.insertText("\n");
        }


    }

};
