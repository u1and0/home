# ST tool
Sublimetext3 で使用しているuser settingやらmacroやらsnippet.  
以下に適当な分類示す。  

+ [keymap & mousemap & setting](#keymap--mousemap--setting)
+ [Theme](#theme)
+ [syntax settings](#syntax-settings)
+ [build series](#build-series)
+ [initial series](#initial-series)
+ [insert date](#insert-date)
+ [line series](#line-series)
+ [Enhanced text](#enhanced-text)
+ [package's sublime setting](#package)
+ [なんだこれ](#なんだこれ)










-----------------------------------------------------------------------


## keymap & mousemap & setting
* Preferences.sublime-settings
  主な設定version わかんない
* Default (Linux).sublime-keymap
* Default (OSX).sublime-keymap
* Default (Windows).sublime-keymap


### UPDATE7.2.7
markdown_preview in browser as ["alt+b"]

### UPDATE7.2.6
show_panel build result as ["ctrl+shift+@"]

### UPDATE7.2.5
Quick Change Project as ["ctrl+alt+p"]

### UPDATE7.2.4
Remove "save_project_as" and "save_workspace_as"
Close work space as ["ctrl+k","ctrl+c"]



### UPDATE7.2.3
{ctrl+e,ctrl+o}Evernote:List Recent Notes  
{ctrl+shift+e,ctrl+shift+o}Evernote:Open Note  



### UPDATE7.2.2
{shift+enter}insert_2spaceNewline.sublime-macro  
	shift + enterで行末にスペース二つ入れてから改行  
	行間のどの位置から実行しても良い  



### UPDATE7.2.1
Auto-pair Back Quotesはスペースを保管しないように変更  



### UPDATE7.2
Auto pair \*  
select内を*でくくる  
他のAuto pairと異なり、何もない行に*を打ち込んだときは通常通り*が打たれる(項目として使われる*, 計算式として使われる*が必要だから)  
Auto pair ~  
打消し線~~が打たれる  
Auto pair  \`    




### UPDATE7.1
Auto-pair percent %の自動補完  
"ctrl+p","ctrl+w" ワークスペースの保存  
"ctrl+e","ctrl+f" evernote search_note  

* Default (Windows).sublime-mousemap  
### UPDATE3.1
	* expand selection to scope
	* PageScroll
	* soft undo & soft redo
	* jump
	* undo & redo
	* Change tabs
	* Select scope~~+ Select all~~

* Default (Windows).sublime-mousemap.txt  
	sublimetext2から拾ってきたマウスマップのデフォルト  
	参考用なので拡張子が.txt  









## Default (Windows).sublime-mousemap  

### UPDATE3.1

+ expand selection to scope
+ PageScroll
+ soft undo & soft redo
+ jump
+ undo & redo
+ Change tabs
+ Selct all
+ Default (Windows).sublime-mousemap.txt  
sublimetext2から拾ってきたデフォルト





-----------------------------------------------------------------------
## Theme
+ [Tubnil_kai.tmTheme](https://github.com/austinwagner/sublime-sourcepawn/blob/master/Tubnil.sublime-theme)  
色を若干変更した。






-----------------------------------------------------------------------
## syntax settings
* C++.sublime-settings
* MQL4.sublime-settings
* HTML.sublime-settings
* Markdown.sublime-settings
* INI.sublime-settings
* Plain text.sublime-settings
* vbdotnet.sublime-settings





-----------------------------------------------------------------------
## build series
* batch.sublime-build
* html.sublime-build
* perl.sublime-build
* platex.sublime-build


-----------------------------------------------------------------------
## initial series
行頭に移動して所定の記号を入力するマクロ及びスニペット郡  
keymapで`ctrl+alt+/`で起動するように設定している  
コメントアウト//のみ`ctrl+/`で起動するようにしてある  
以下initialフォルダの中身  
* Comments (C++).tmPreferences
	mt4コメントアウトをC++のシンタックスと合わせた
* comment_out.sublime-macro  
	 `Enhanced text`のコメントアウト  
* comment_out_bat.sublime-macro  
	batchのコメントアウト  
* comment_out_vbnet.sublime-macro  
	VB.NETのコメントアウト  
* Default (Windows).sublime-keymap  
	ショートカットで起動できるように登録  
* initial_mark.sublime-macro  
	選択範囲を行ごとにキャレット分割して行頭にキャレット持ってきて以下のスニペット起動
* initial_at.sublime-snippet  
	@を挿入
* initial_dat.sublime-snippet  
	・を挿入
* initial_ket.sublime-snippet  
	引用符>を挿入
* initial_minus.sublime-snippet  
	ハイフンを挿入
* initial_plus.sublime-snippet  
	+を挿入
* initial_sharp.sublime-snippet  
	#を挿入
* initial_star.sublime-snippet  
	*を挿入
* initial_Wslash.sublime-snippet  
	//を挿入(コメントアウト)




-----------------------------------------------------------------------
## insert date
ページのトップにアンダースコア２つと今日の日付を入れる  
**package insertdate**が必要
* insertdate.sublime-macro



-----------------------------------------------------------------------
## line series
-,=,*,_を入力した後にtabキー押すとその文字を20字くらい打って線にしてくれる。  
中央にコメントも入れられる。  
* line_double.sublime-snippet
* line_single.sublime-snippet
* line_star.sublime-snippet
* line_under.sublime-snippet




-----------------------------------------------------------------------
## Enhanced text
自分用シンタックス。.txtや.md形式のファイルをより見やすくするために作った

+ EnhancedTXT.sublime-settings
+ EnhancedTXT.tmLanguage
+ EnhancedTXT.YAML-tmLanguage



##### UPDATE3.3.0

変更リスト

+ --以下色変更
+ []内色変更
+ @とスペース2つに囲まれた文字をハイライト(スペース1つまでならハイライト対象)に変更
+ \#以下のハイライト
	- 行頭にある#1個以上+半角スペースは見出し
	- 行頭にない#1個以上+半角スペースはコメントアウト
+ ()内のハイライト
	- 文字列はコメントアウト
	- 数字は強調


###### @とスペース２つ以上で囲まれた文字列
`"match": "@\\S+\\s{2}"`
<ハイライトして欲しい>
(@のあとにスペース2つ)
@ja  
(@のあとにスペース1つ行末)
@ja 
@ja あ
(@のあとにスペースなし)
@ja
(スペース2つで区切られていれば、その後の文字列はハイライト無効)
@textenhanced  zgg @loman  
(間にスペースがひとつでも入るとハイライト無効)
@text enhanced  zgg @loman  
@text enhanced  zgg @loman ad
@text enhanced  
@text  enhanced@ccom
<(一部または全部)ハイライトして欲しくない>
(間にスペースが入った場合)
@text enhanced   @loman ad  
(メールアドレス)
mailaddress@gmail.com
(スペースひとつでハイライト無効)
mailaddress@gmail.com jhf
(スペース二つはいるとハイライト有効)
mailaddress@gmail.com  jhf
(末尾にスペースが2つない)
EnhancedText @趣味 aa@ja
(文頭@文末スペース２つでも、間に挟まれた文字列が@とスペースにはさまれていなければハイライト無効)
@家  zz @金銭 z  @aasdfg  




###### ()内
`"match": "\\([\\)_,\\.\\-\\s\\d]+\\)"`
`"match": "(?<=[^\\]])\\([\\w\\s^\\)]+\\)"`
数字・記号が1つでも入るとコメント
文字列はコメント
__TEST__
http:asdf    #httpは
https:asjkf
(https:asjkf)
](https:asjkf)
(hoge)   スペースが一個でも入るとコメントアウト
(hoge)スペース含まれなければ通常(リンクとかぶる)
(1)    数字、記号は強調
(1.4746 12343 42  3 4523, 534)    数字、記号は強調(123)後ろにまたカッ(a)コが来ても区別してくれる[](hadfttps)
(1_47-4 6)    数字、記号、スペースは強調
(1-47a-46)    数字、記号以外が入るとはコメント
(comment out)    文字列はコメントアウト
________________________


###### []内の文字
`"match": "\\[+[^\\]]+\\]+"`
色変更


###### #以下の文字
`"match": "\\#+\\s(\\s|.)*"`

**#が行頭にあった場合**

- 強調
- 色変更
- entity.name.typeにすることでctrl+rから検索できる





**#が行頭にない場合**

- コメントアウト
- //と使い分けるためにブロックコメント色を使用


__TEST__
normal#normal
normal      # comenntout
normal		# comenntout
#normal# commentout
normal# comment out
	# comment out
	normal# commentout
# heading# heading
# heading # heading
# heading
____________________________

###### /**/に囲まれた文字列(擬似ブロックコメントアウト)
**"match": "(/\\*\\s[^(\\*/)]*\\*/|/\\*\\s([^(\\*/)]|\\s)*|.*\\s\\*/)",**
改行がわからないから行頭まで行末までを有効
"/*半角スペース<文字列>*/"の間
"/*半角スペース"の後ろ
"半角スペース*/"の前

__TEST__
/*normal*/
/*normal
normal*/
/*comment */normal
/* comment */normal
/* comment */ normal/* comment*/normal

/* comment
comment */
comment */

normal/* comment

normal/* comment           comment            */
	normal
	normal */normal

comment */normal
				comment */normal
normal*/normal
____________________________




##### UPDATE3.1.2
+ カッコ内がシャープ始まりでも色変え(markdonwのページないアンカー)
+ 斜線、太字のコメント変更


##### UPDATE3.1.1
+ 斜線、太字の不具合を修正
	+ 米マークが先頭に来ていても色が変わるように修正
	+ 同じ行に斜線、太字マークが複数あっても色が変わる

##### UPDATE3.1
+ <>の色を緑に変更
	- 元々緑だった@は紫に変更
+ 項目番号の表示修正
	- 2桁以上の数字に対応できるようにした
	- 行頭だけではなく、先頭文字がスペースまたはタブでも色変え対象とした  
		`{"match": "(\\s|^)\\d+\\.\\s",




##### UPDATE3.0
+ MarkDown記法への対応  
	- [ライン]ハイフン2個以上並んだとき、以下を色変え  
	- [項目]+,-,*とスペース  
	- [数字項目]数字とドット  
	- [ボールド体]アスタリスク*2個のならびに囲まれた文字  
	- [イタリック体]アスタリスク*1個のならびに囲まれた文字  
	- [打ち消し文字]チルダ~2個のならびに囲まれた文字  
	- [コード]バッククォート\`内、及びバックォート\`以下  
	- [リンク]\(\)内のhttp,https以下の文字  
	- [見出し]シャープ#1個以上とスペースがついたとき以下の色変え  
+ カッコの修正  
	- シングル・ダブルクオート内の色変えの修正  
	- 色変えに対応したカッコのを増やした(飾りカッコや全角＜＞)  
	- 角カッコは2重以上でも色がつく  
+ その他  
	- @マーク以下の色変えは閉じ文字としてスペース2つ以上  
	- *マーク後にスペース入れなきゃ色変えしないようにした  
	- ブロックコメントアウト/*は削除  







-----------------------------------------------------------------------
## package's sublime setting
導入しているpackageのセッティング  
使っているpackage見たいときはPackage Control.sublime-settings参照
* insert_date.sublime-settings
* Package Control.sublime-settings
* Side Bar.sublime-settings
* trailing_spaces.sublime-settings
* ~~Evernote.sublime-settings~~		token含まれているからignore



-----------------------------------------------------------------------
## なんだこれ
* ST_csv_edt.sublime-macro







