# Bana OCR

Thực hiện Text Detection và Extraction trên dữ liệu là hình ảnh của từ điển Tiếng Bana.
Công cụ sử dụng:

- Python
- Tesseract
- OpenCV
- Cùng một số thư viện của Python khác...

## Tính năng

- Nhận diện chữ đánh máy/ viết tay có trong 1 hình ảnh đầu vào
- Từ đó rút trích ra tiếng Việt vào định dạng file txt (chưa có format/định dạng)
- Sau đó sử dụng các hàm Heuristics để chuyển sang tiếng Bana

|Gốc |Chuyển sang|
|----|----|
| ð  | ơ̆  |
| ẽ  | ĕ  |
| ¡  | i  |
| mĩ | mĭ |
| ợ  | ơ  |
| ồ  | ŏ  |
| ố  | ơ̆  |
| ỗ  | ô̆  |
| ơi | ơĭ |
| ổi | ôĭ |
| š  | ĕ  |
| Š  | ê̆  |
| ủ  | ŭ  |
| Ủ  | Ŭ  |
| ũ  | ŭ  |
| Ũ  | Ŭ  |

## Sử dụng

- Thư mục "input": chứa các hình ảnh cần xử lý, lý tưởng là mỗi hình ảnh chứa 1 trang của từ điển tiếng Bana
- Thư mục"output": Kết quả trích xuất OCR
- Thư mục "result": Kết quả sau khi chạy correction với Heuristics

Đầu tiên chạy:
```
python run.py
```
Sau đó:
```sh
python correction.py
```

## Hạn chế

Dù chức năng chính là rút trích tiếng Bana đã được hiện thực, project còn một vài hạn chế:
- Chưa format lại kết quả (ví dụ: in đậm, in nghiêng, font chữ to, nhỏ,...) như văn bản gốc
- Chưa có xử lý kết quả với các input không phải là text thuần, ví dụ như bảng biểu, một trang có nhiều cột,...
- Kết quả rút trích tiếng Bana sử dụng Tesseract, nhưng hiện tại Tesseract, cũng như các model OCR khác chưa hỗ trợ tiếng Bana, nên kết quả là từ rút trích dưới dạng Tiếng Việt, sau đó sử dụng một vài hàm Heuristics để sửa các lỗi thường gặp


## Tác giả

[Tran Khanh Tung](https://github.com/KhanhTungTran)
