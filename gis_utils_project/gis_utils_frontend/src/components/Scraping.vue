<template>
  <div>
    <h1 class="mt-4">Scraping</h1>
    <h2>担当会社情報ステータス</h2>
    <table class="table table-bordered table-hover">
        <thead>
            <tr>
                <th>法人名</th>
                <th>更新日時</th>
                <th>更新ステータス</th>
                <th>更新ボタン</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <th>新日本</th>
                <td>-</td>
                <td>-</td>
                <td><button class="btn btn-sm btn-primary" type="submit">更新</button></td>
            </tr>
            <tr>
                <th>あずさ</th>
                <td>-</td>
                <td>-</td>
                <td><button class="btn btn-sm btn-primary" type="submit">更新</button></td>
            </tr>
            <tr>
                <th>トーマツ</th>
                <td>-</td>
                <td>-</td>
                <td><button class="btn btn-sm btn-primary" type="submit">更新</button></td>
            </tr>
            <tr>
                <th>あらた</th>
                <td>-</td>
                <td>-</td>
                <td><button class="btn btn-sm btn-primary" type="submit">更新</button></td>
            </tr>
        </tbody>
    </table>
  </div>
</template>
<script>
export default {
  name: 'Scraping'
}
</script>

<style>
</style>
