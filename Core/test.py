from tracker import create_new_session

# 创建 root
root_id = create_new_session(
    file_path="test.ptx",
    parent_id=None
)

print("Created root:", root_id)

# 模拟你修改文件后再保存
v2_id = create_new_session(
    file_path="test1.ptx",
    parent_id=root_id
)

print("Created v2:", v2_id)