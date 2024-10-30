# Model 目录

## 概述
该目录包含了与用户信息、节点信息、请求信息和区块链相关的数据库模型。这些模型使用 SQLAlchemy 进行定义，并且继承自 `BaseModel`，以便自动管理创建和更新的时间戳。

为了确保数据的不可篡改性和可追溯性，我们使用区块链技术将过去10分钟内的信息封装成一个区块。例如，在3点20分时，记录3点到3点10分的内容。所有节点都会封装这个区块，并进行一次共识广播。如果在共识广播时发现周围节点记录的区块与自身不一致且超过3次，该节点将丢弃自己的区块并同步其他节点的区块。

## 模型定义

### BaseModel
`BaseModel` 是所有模型的基类，定义了两个自动管理的时间戳字段：
- `created_at`: 记录模型创建的时间。
- `updated_at`: 记录模型最后一次更新的时间。

定义在 [basemodel.py](basemodel.py) 中。

### Account 模型
`Account` 模型用于存储账户信息。主要字段包括：
- `identifier`: 唯一标识符，一般是一个合法的 UUID。
- `nickname`: 用户昵称。
- `change_chat_id_time`: 更换聊天标识符的时间。
- `public_key`: 用户的公钥。
- `message_server`: 消息服务器的地址。
- `signature`: 上一次的签名，用于验证账户的合法性。

定义在 [account.py](account.py) 中。

### Node 模型
`Node` 模型用于存储连接到的节点信息。主要字段包括：
- `address`: 节点地址。
- `port`: 节点端口。
- `status`: 节点状态（在线/离线）。
- `delay`: 节点延迟。

定义在 [node.py](node.py) 中。

### Request 模型
`Request` 模型用于存储请求信息。主要字段包括：
- `identifier`: 唯一标识符，一般是一个合法的 UUID。
- `account_identifier`: 请求指向的账户标识符。
- `content`: 请求的内容。

定义在 [request.py](request.py) 中。

### Block 模型
`Block` 模型用于存储区块信息。主要字段包括：
- `identifier`: 唯一标识符，一般是一个合法的 UUID。
- `timestamp`: 区块的时间戳，表示区块封装的时间。
- `content`: 区块的内容，存储过去10分钟内的信息。
- `previous_hash`: 上一个区块的哈希值，用于链式结构。
- `current_hash`: 当前区块的哈希值，用于验证区块的完整性。
- `status`: 区块的状态，表示是否已被广播并确认。

定义在 [block.py](block.py) 中。