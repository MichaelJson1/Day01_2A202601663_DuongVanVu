# K3 — Ngày 1: Bài Tập & Phản Ánh
## Khám Phá LLM API | Phiếu Thực Hành

**Thời lượng:** 9h00–13h00
**Cách làm:** Trả lời từng câu ngay sau khi hoàn thành block tương ứng —
đừng để dồn hết về cuối buổi. Thay dòng `*Câu trả lời của bạn*` bằng câu
trả lời thật (chấm tự động sẽ đếm số câu đã trả lời).

---

## Block 1 — API Cơ Bản (trả lời sau Checkpoint 1)

### Câu 1.1 — Độ nhạy của temperature
Gọi `call_openai` với temperature 0.0, 0.5, 1.0 và 1.5 dùng prompt
**"Hãy kể cho tôi một sự thật thú vị về Việt Nam."**

**Bạn nhận thấy quy luật gì qua bốn phản hồi?** (2–3 câu)
> Khi temperature tăng từ 0.0 lên 1.5, câu trả lời có xu hướng đa dạng và sáng tạo hơn. 
> Ở temperature 0.0, phản hồi thường ngắn gọn, ổn định và ít thay đổi; 
> còn ở mức 1.0–1.5, cách diễn đạt phong phú hơn nhưng đôi khi dài dòng hoặc chứa thông tin kém chính xác hơn.

### Câu 1.2 — Chọn temperature cho sản phẩm
**Bạn sẽ đặt temperature bao nhiêu cho chatbot hỗ trợ khách hàng, và tại sao?**
> Với chatbot hỗ trợ khách hàng, temperature khoảng 0.2 - 0.3 sẽ phù hợp.
> Mức temperature thấp giúp câu trả lời nhất quán, tập trung vào thông tin chính xác và hạn chế việc model 
> tự suy đoán, đồng thời vẫn đủ tự nhiên khi giao tiếp với người dùng.

### Câu 1.3 — Đánh đổi chi phí
Kịch bản: 10.000 người dùng hoạt động mỗi ngày, mỗi người gọi API 3 lần,
mỗi lần trung bình ~350 token đầu ra.

**Ước tính GPT-4o đắt hơn GPT-4o-mini bao nhiêu lần cho workload này? Nêu một
trường hợp GPT-4o xứng đáng với chi phí và một trường hợp nên dùng mini:**
> Mỗi ngày hệ thống tạo khoảng: 10.000 x 3 x 350 = 10.500.000 token đầu ra
> Theo bảng giá, chi phí ước tính cho GPT-4o là $105/ngày, cho GPT-4o-mini là $6.3/ngày.
> Giá GPT-4o đắt gấp 16.7 lần GPT-4o-mini.
> GPT-4o phù hợp trong các trường hợp cần suy luận phức tạp, ví dụ phân tích các vi chất trong cơ thể và 
> gợi ý món ăn phù hợp. GPT-4o-mini phù hợp với các tác vụ đơn giản và có số lượng yêu cầu lớn như trả lời
> các chính sách của công ty.

---

## Block 2 — System Prompt & Token (trả lời sau Checkpoint 2)

### Câu 2.1 — Sức mạnh của persona
Gọi `chat_with_system_prompt` hai lần với cùng câu hỏi
**"Giải thích blockchain là gì?"** nhưng hai system prompt khác nhau:
- "Bạn là giáo viên tiểu học, giải thích thật đơn giản cho trẻ 8 tuổi."
- "Bạn là chuyên gia tài chính, trả lời chuyên sâu bằng thuật ngữ kỹ thuật."

**Hai phản hồi khác nhau như thế nào (độ dài, từ vựng, ví dụ)? System prompt
ảnh hưởng đến hành vi model ra sao?** (3–4 câu)
> Đối với system prompt giáo viên tiểu học, độ dài của câu trả lời thường ngắn hơn, các từ vựng, ví dụ cũng gần
> gũi và trực quan hơn.
> Đối với system prompt chuyên gia tài chính, độ dài của câu trả lời dài và chuyên sâu hơn, sử dụng nhiều thuật 
> ngữ chuyên ngành và ví dụ tập trung vào cấu trúc và ứng dụng tài chính.
> Điều này cho thấy, system prompt có thể điều chỉnh vai trò, độ chuyên sâu và cách trình bày của model.

### Câu 2.2 — tiktoken vs đếm từ
Chọn một đoạn văn tiếng Việt ~100 từ. So sánh số token theo `count_tokens`
(tiktoken) với ước lượng `số từ / 0.75` mà Part 1 đã dùng.

**Hai con số chênh nhau bao nhiêu phần trăm? Vì sao tiếng Việt thường tốn
nhiều token hơn tiếng Anh cùng độ dài?**
> Ví dụ chọn một đoạn văn 102 từ, số token tính theo tiktoken là 132, token ước lượng là 136
> Chênh lệch là 2.94%
> Prompt tiếng Việt thường tốn nhiều token hơn tiếng Anh cùng độ dài vì các từ có dấu và nhiều chuỗi tiếng Việt
> có thể bị tách ra thành nhiều đơn vị nhỏ hơn

---

## Block 3 — Streaming & Độ Bền (trả lời sau Checkpoint 3)

### Câu 3.1 — Trải nghiệm người dùng với streaming
**Streaming quan trọng nhất trong trường hợp nào, và khi nào thì
non-streaming lại phù hợp hơn?** (1 đoạn văn)
> Streaming giúp model gửi từng phần của câu trả lời ngay khi chúng được tạo ra, thay vì chờ toàn bộ phản hồi 
> hoàn thành. Non-streaming phù hợp hơn khi phản hồi ngắn, khi chương trình cần nhận toàn bộ kết quả trước khi 
> xử lý, hoặc khi không muốn hiển thị nội dung chưa hoàn chỉnh. Streaming phù hợp khi muốn cải thiện trải nghiệm
> của người dùng để họ có thể đọc câu trả lời gần như lập tức, đặc biệt với các câu trả lời dài.

### Câu 3.2 — Vì sao backoff theo cấp số nhân?
**So với delay cố định (ví dụ luôn chờ 1 giây), exponential backoff có lợi
thế gì khi API bị quá tải? Điều gì xảy ra nếu hàng nghìn client cùng retry
với delay cố định giống nhau?**
> Exponential backoff là cơ chế tăng dần thời gian chờ sau mỗi lần gọi API thất bại. Với base_delay = 0.1, 
> thời gian chờ có thể lần lượt là 0,1 giây, 0,2 giây và 0,4 giây. Cơ chế này giúp giảm số lượng request gửi 
> liên tục khi server đang quá tải hoặc gặp lỗi tạm thời.
> Nếu hàng nghìn client đều thử lại sau cùng một khoảng thời gian cố định, chúng có thể đồng loạt gửi request 
> trở lại server và tiếp tục gây quá tải. Hiện tượng này được gọi là “thundering herd”. Có thể giảm hiện tượng 
> này bằng cách kết hợp exponential backoff với jitter, tức là thêm một khoảng thời gian ngẫu nhiên vào mỗi lần 
> chờ.

---

## Block 4 — Mini-Project (trả lời sau Checkpoint 4)

### Câu 4.1 — Thiết kế persona
**Bạn chọn persona gì cho trợ lý của mình? Viết lại system prompt đó và giải
thích 1–2 lựa chọn từ ngữ quan trọng trong prompt (ví dụ: vì sao yêu cầu
"trả lời ngắn gọn", vì sao chỉ định ngôn ngữ...):**
> Persona của tôi là trợ giảng AI thân thiện, giải thích từng bước bằng tiếng Việt và đưa ví dụ Python khi cần.
> System prompt: “Bạn là trợ giảng AI thân thiện, giải thích từng bước bằng tiếng Việt, sử dụng từ ngữ dễ hiểu 
> và đưa ra ví dụ Python ngắn khi cần. Nếu không chắc chắn về thông tin, hãy nói rõ thay vì tự suy đoán".
> Tôi chọn persona này vì trợ lý được sử dụng trong quá trình học lập trình và trí tuệ nhân tạo. Cụm từ “giải 
> thích từng bước” giúp câu trả lời có cấu trúc và dễ theo dõi. Yêu cầu “sử dụng từ ngữ dễ hiểu” giúp hạn chế 
> việc dùng quá nhiều thuật ngữ kỹ thuật. Phần “đưa ra ví dụ Python ngắn khi cần” làm phản hồi có tính thực hành 
> hơn. Cuối cùng, yêu cầu nói rõ khi không chắc chắn giúp giảm nguy cơ model tạo ra thông tin sai nhưng trình bày 
> như một sự thật.
### Câu 4.2 — Hạn chế & cải thiện
**Trợ lý của bạn hiện có hạn chế lớn nhất là gì (ví dụ: history chỉ 3 lượt,
không có bộ nhớ dài hạn, không kiểm duyệt nội dung...)? Đề xuất một cải
thiện cụ thể và mô tả ngắn cách triển khai:**
> Một hạn chế của trợ lý hiện tại là chỉ lưu ba lượt hội thoại gần nhất. Khi cuộc trò chuyện kéo dài, trợ lý có 
> thể quên các yêu cầu hoặc thông tin quan trọng đã xuất hiện ở đầu phiên. Có thể cải thiện bằng cách tóm tắt nội 
> dung cũ trước khi xóa khỏi history, sau đó thêm bản tóm tắt đó vào system message hoặc lưu trong cơ sở dữ liệu.
> Ngoài ra, trợ lý chưa có khả năng kiểm chứng thông tin bằng nguồn bên ngoài nên vẫn có thể tạo ra câu trả lời 
> không chính xác.
---

## Danh Sách Kiểm Tra Nộp Bài

- [ ] `python grade.py` — xem điểm tự động, mục tiêu ≥ 75/100
- [ ] Cả 4 checkpoint pytest đều pass
- [ ] Tất cả 9 câu trong file này đã được trả lời
- [ ] Đã copy bài làm vào folder `solution/` và zip theo hướng dẫn README
