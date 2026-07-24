from template import count_tokens


text = """
Trí tuệ nhân tạo đang trở thành quen thuộc trong đời sống hiện đại.
Công nghệ này được sử dụng trong giáo dục, y tế, tài chính, giao thông
và các lĩnh vực khác. Nhờ khả năng phân tích dữ liệu lớn, hệ thống
thông minh có thể hỗ trợ con người đưa ra quyết định nhanh hơn.
Tuy nhiên, trí tuệ nhân tạo cũng đặt ra vấn đề về quyền riêng tư,
minh bạch và trách nhiệm. Vì vậy, người phát triển cần sử dụng công
nghệ cẩn trọng, có đạo đức và kiểm tra độ chính xác của kết quả.
""".strip()

word_count = len(text.split())
actual_tokens = count_tokens(text)
estimated_tokens = word_count / 0.75

difference_percent = (
    abs(actual_tokens - estimated_tokens)
    / estimated_tokens
    * 100
)

print("Số từ:", word_count)
print("Token theo tiktoken:", actual_tokens)
print("Token ước lượng:", round(estimated_tokens, 2))
print("Chênh lệch:", round(difference_percent, 2), "%")