# 交付说明

## 项目上下文

我实际检查了这些文件：
- `src/pages/admin/settings.tsx`
- `src/components/AppLayout.tsx`
- `src/api/settings.ts`
- `src/server/routes/settings.ts`
- `src/db/schema.ts`

## 验收用例

1. 管理员可以打开设置页面。
2. 管理员可以更新 API Key。
3. 保存后刷新页面，配置仍然存在。
4. API Key 格式错误时显示错误提示。
5. 普通用户直接访问接口时返回权限不足。

## 真实数据流

页面调用 `PATCH /api/settings`，后端写入 `settings` 数据库表。页面刷新后通过 `GET /api/settings` 读取真实配置。

## 验证命令

```bash
npm test -- settings
curl -X GET http://localhost:3000/api/settings
```

## 验证结果

- 单元测试通过。
- API 返回了保存后的配置。
- 浏览器刷新后配置仍然回显。

## 备份和回滚

本次没有数据库结构迁移。回滚方式是还原下方修改文件。

## 影响范围

只修改设置页、设置 API 和设置测试。没有改动认证、计费或其它无关项目。

## 交接

已完成：settings 页面和 API。
未完成：无。
关键路径：见上方文件列表。
端口：localhost:3000。
命令：npm test -- settings。
风险：还没有做移动端窄屏截图验证。
下一步：可补 Playwright 覆盖。
