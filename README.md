# ePaperPi

ePaper のためのライブラリです。
オリジナルのライブラリはjairoshさんの
https://github.com/jairosh/raspberrypi-ssd1680/tree/master
です。
こちらは 「WeAct Studio 2.13" three-color e-paper display」用のものですが、
これを　WeAct Studio 2.9 白黒 用に改造したものになります。

<h4><<概要>></h4>
　ePaper2.9インチ表示器一式とラズパイ装着用基板です。 <br>
　サンプルプログラムとして、ePaper表示用のライブラリとタイマー表示と時計プログラムがあります。 <br>
　すべてのソースプログラムを開示いたします。 <br>

・部品の仕様が変わる場合があります。 <br>
・基板のバージョンが変わる場合がありますが、機能等に違いはありません。<br>
・ラズパイは付属しません。<br>

<h4><<使用方法>></h4>
git clone https://github.com/momorara/ePaperPi <br>
でラズパイにダウンロードしてください。<br>
インストールについては、インストール文書に従いインストールを行ってください。<br>
説明写真のような使い方ができます。<br>

<h4><<使用説明資料>></h4>
説明書類の中の資料を確認ください。
お問い合わせに関しては、サポート.txtを参照ください。<br>

<h4><<動作環境>>></h4>
2024/7/27 対応OS：Bullseye版(11.10)での動作を確認しました。<br>
2024/7/27 Pi5 BookWormでは動作確認できていません。<br>
2024/12/30 対応OS：Bullseye版(11.11)での動作を確認しました。<br>
2025/01/11 新プログラムで、対応OS：Bullseye版(11.11)での動作を確認しました。 <br>
2025/01/11 新プログラムで、Pi5 対応OS：BookWorm版(12.8)での動作を仮想環境にて確認しました。 <br>
2025/01/19 新プログラムで、Pi5 対応OS：BookWorm版(12.8)での動作を確認しました。 <br>
仮想環境なしでもインストール、動作可能になりました。<br>
2025/02/14 新プログラムで、Pi5 対応OS：BookWorm版(12.9)での動作を確認しました。<br>
2025/02/19 新プログラムで、対応OS：Buster版(10.13)での動作を確認しました。<br>
  
<h4><<ライセンス>></h4>
GNU General Public License v3.0 <br>
使用しているライブラリについては、ライブラリ制作者のライセンス規定を参照ください。 <br>
オリジナル部分についても同様とします。 <br>
プログラム自体はサンプルプログラムです。 <br>

<h4><<メンテナンス情報>>></h4>
2025/01/10 RPi.GPIOを使わないgpiozero方式とした<br>
ドライバーの都合なのか物理的には 128*296 のはずだが、128*292 の表示領域となります。<br>

<h4><<サポート窓口>></h4>
  メールアドレスが　tkj-works@mbr.nifty.com に変更になっています。<br>
  資料等を修正中ですが、ご注意ください。<br>
  サポートコミュニティー　https://www.facebook.com/groups/3773038759434230<br>
