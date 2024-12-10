これは、Tobii Pro Labのデータエクスポートのヘッダーであり、視線追跡および関連データに関するさまざまな情報が含まれています。それぞれの列を簡単に説明します。

---

### **タイムスタンプ関連**
- **Recording timestamp**  
  録画のタイムスタンプ（Tobii Pro Labで記録開始からの経過時間）。
- **Computer timestamp**  
  コンピュータのシステム時刻（録画データに対応するPCのローカル時間）。

---

### **プロジェクト・参加者情報**
- **Sensor**  
  使用したセンサーの種類。
- **Project name**  
  プロジェクトの名前。
- **Export date**  
  データがエクスポートされた日付。
- **Participant name**  
  参加者の名前。
- **Recording name**  
  録画データの名前。
- **Recording date**  
  録画の実行日。
- **Recording date UTC**  
  協定世界時（UTC）での録画日。
- **Recording start time**  
  録画開始時刻（ローカル時間）。
- **Recording start time UTC**  
  録画開始時刻（UTC）。
- **Recording duration**  
  録画の継続時間。

---

### **視線データ**
- **Recording Fixation filter name**  
  使用した視線固定（Fixation）フィルターの名前。
- **Event**  
  イベントの種類（例えば、「視線固定」や「サッケード」など）。
- **Event value**  
  イベントに関連する値（例えば、サッケードの速度や固定の時間など）。
- **Gaze point X / Y**  
  視線点のスクリーン上の2D座標。
- **Gaze point 3D X / Y / Z**  
  視線点の3D空間における座標。
- **Gaze direction left/right X / Y / Z**  
  左目と右目の視線方向ベクトル（3D空間）。
- **Pupil position left/right X / Y / Z**  
  瞳孔の空間的位置（3D空間）。
- **Pupil diameter left/right**  
  左目と右目の瞳孔径。
- **Pupil diameter filtered**  
  フィルタリング処理後の瞳孔径。
- **Validity left/right**  
  左目と右目のデータの有効性（信頼性の指標）。

---

### **マッピングデータ**
- **Assisted mapping gaze point X/Y**  
  Tobii Pro Labの「アシストマッピング」機能で補正された視線点。
- **Manually mapped gaze point X/Y**  
  手動でマッピングされた視線点。
- **Mapped gaze point X/Y**  
  最終的に使用されたマッピング後の視線点。
- **Assisted mapping gaze point score**  
  アシストマッピングにおけるスコア（精度の評価）。

---

### **録画メディア情報**
- **Recording media name**  
  録画に使用したメディアの名前。
- **Recording media width / height**  
  録画メディアの幅と高さ（ピクセル単位）。
- **Width / Height**  
  データエクスポート時に指定したメディアの幅と高さ。

---

### **視線の種類**
- **Mapped eye movement type**  
  マッピング後の視線移動の種類（例: 固定、サッケード、滑動）。
- **Mapped eye movement type index**  
  上記視線移動の種類に対応するインデックス。
- **Mapped fixation X / Y**  
  マッピング後の視線固定点（スクリーン座標）。
- **Eye movement type**  
  視線移動の種類（例: 固定、サッケード、滑動）。
- **Gaze event duration**  
  視線イベントの継続時間。
- **Eye movement type index**  
  視線移動タイプのインデックス。

---

### **加速度センサーとジャイロデータ**
- **Gyro X / Y / Z**  
  ジャイロセンサーのデータ（X, Y, Z軸）。
- **Accelerometer X / Y / Z**  
  加速度センサーのデータ（X, Y, Z軸）。
- **Magnetometer X / Y / Z**  
  磁気センサーのデータ（X, Y, Z軸）。

---

これらのデータは視線追跡や行動解析において非常に有用であり、被験者の視覚的注目点、視線の動き、環境との相互作用を分析するために利用されます。