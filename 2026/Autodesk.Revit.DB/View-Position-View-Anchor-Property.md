# View Position View Anchor Property

Source: https://www.revitapidocs.com/2026/39095e75-5102-8afe-8d52-e817d9227cc5.htm

---

| View Position View Anchor Property |
| --- |

Specifies the method by which the view will be positioned on the sheet. Default is set to ViewAnchor.ViewOrigin. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public ViewAnchor ViewAnchor { get; set; }
```

```
Public Property ViewAnchor As ViewAnchor
	Get
	Set
```

```
public:
property ViewAnchor ViewAnchor {
	ViewAnchor get ();
	void set (ViewAnchor value);
}
```

```
member ViewAnchor : ViewAnchor with get, set
```

#### Property Value

[ViewAnchor](View-Anchor-Enumeration.md) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[ViewPosition Class](View-Position-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
