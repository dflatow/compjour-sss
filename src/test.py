from bs4 import BeautifulSoup


data = """
<table>
    <tr>
        <td>1</td>
        <td>2</td>
        <td>3</td>
    </tr>

    <tr>
        <td>4</td>
        <td>5</td>
        <td>6</td>
    </tr>

    <tr>
        <td>7</td>
        <td>8</td>
        <td>9</td>
    </tr>
</table>
"""


soup = BeautifulSoup(data)
for td in soup.select('table > tr:nth-of-type(2)'):
    print("a", td)
    print(td.text)