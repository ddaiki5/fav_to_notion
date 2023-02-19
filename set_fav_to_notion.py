from notion_client import Client
import os




def setting_client():
    token = os.environ.get("NOTION_TOKEN")

    client = Client(auth=token)
    
    return client

# ページに子ページを追加する関数
def add_child_page(client, content, urls):
    database_id = os.environ.get("DATABASE_ID")
    # 子ページのプロパティ（タイトル）を設定
    properties = {
        "title": {
            "type": "title",
            "title": [
                {
                    "type": "text",
                    "text": {
                        "content": content[:10]
                    }
                }
            ]
        }
    }

    # 子ページのブロック（本文）を設定
    children = [
        {
        "object": "block",
        "type": "paragraph",
            "paragraph": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": content
                        }
                    }
                ]
            }
        }
    ]

    # 子ページを作成するAPIを呼び出す
    response = client.pages.create(parent={"database_id": database_id}, properties=properties, children=children)
    print(urls)
    for url in urls:
        client.blocks.children.append(block_id=response["id"], children=[{"object": "block", "type": "image", "image": {"type": "external", "external": {"url": url}}}])
    
def add_pages(client, fav_list):
    for content, urls in fav_list:
        s = "\n".join(content)
        add_child_page(client, s, urls)


