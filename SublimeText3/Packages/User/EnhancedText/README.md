# EnhancedText ver3.4.1

#### UPDATE3.4.1
行頭の<=2個以上>の並び 色変え
README追加

#### UPDATE3.3.1
()内コメントアウト　行頭でも有効なように修正

## INTRODUCTION
自分用シンタックスハイライト
markdownサポート

## ACTION
YAML形式でハイライトを設定

## USAGE
Built by PackageDev

## PLAN
行変えしてもルール継続する方法ないんか？


rules
-------------------

```text
  下にある方が優先度高い
  '^'はひとつ前の文字の指定
  '\\s' 半角スペースorTab
  '\\S'は半角スペース置かなかったら有効
  '\\S*'は次のスペースかタブが来るまで続く文字列指定
  '\\t'タブ
  [1-9]とすれば1から9まで
  [a-z]とすればaからzまで
  '\\('は手前括弧。逆も同様
  '*'は同様の文字列が続いたとき
  '.*'はそれ以下のどんな文字列でも
  '.' なんでも1文字の意味
     '.+' 好きな文字いくらでも
  '(a|b)'でaまたはb
  '\\d'が数字
     '\\d{4}'で数字４つ
     '\\d+'でdいくつでもという意味
  '\\\\.'でdot
  '+'はその前の同じ文字１文字以上でも
  (\\\\s|.)*スペースも文字も含む
  (参考)([1-2]\\d{3}[-/\\\\.](0?[1-9]|1[012])[-/\\\\.](0[1-9]|[12]\\d|3[01])
  ){1,2}で日付表示
    '\\\\d{3}.*'で数字が３つ続いたらその後はずっと色変え
```

color
-------------------------------------------------------------------------
Using Color Scheme 
Theme-Nil
Color Scheme-Tubnil_kai << customed Tubnil (Sankasan)

```text
  -------------------------------------------------------------------------
  foreground pink / red  (markup.deleted.git_gutter)
  foreground red / white  (invalid)
  -------------------------------------------------------------------------
  background skyblue / skyblue   (meta.package)
  background palepink / red   (entity.name.type)
  background palepink / pink   (entity.name.function)
  background purple / white   (meta.diff.git-commit)
  background light purple / white   (punctuation.definition.unchanged.diff)
  background mint green / white   (markup.inserted)
  background blue / white   (meta.diff.header)
  background green / yellow   (markup.inserted.git_gutter)
  background orange / orange   (keyword.control.memory)
  -------------------------------------------------------------------------
  red   (constant.character.escaped)
  yellow(orrange)   (markup.changed.git_gutter)
  blue(orrange)   (constant)
  dark blue(dark orrange)   (keyword.operator)
  dark sky blue(brown)   (support.type)
  pale pink(brown)   (punctuation.definition.string.begin)
  yellow(green)   (entity.name.tag)
  yellow(green)   (meta.tag)
  green(moss green)   (support.function)
  purple   (support.constant)
  gray   (source comment.block)
  gray   (comment)
  red orange(green blue)   (storage)
  blue   (variable.language)
  blue   (keyword.control.import)
  purple   (variable.other.constant/constant.numeric)
  skyblue(light purple)   (keyword)
  pink    (entity.other.inherited-class)
  dark pink   (keyword.control)
```
