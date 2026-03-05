# Stairs Path Type Start Symbol Type Id Property

Source: https://www.revitapidocs.com/2026/9d3eb283-4348-8330-99f9-6440074e7aaf.htm

---

| Stairs Path Type Start Symbol Type Id Property |
| --- |

The start symbol type of stairs path. 
**Namespace:** [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public ElementId StartSymbolTypeId { get; set; }
```

```
Public Property StartSymbolTypeId As ElementId
	Get
	Set
```

```
public:
property ElementId^ StartSymbolTypeId {
	ElementId^ get ();
	void set (ElementId^ value);
}
```

```
member StartSymbolTypeId : ElementId with get, set
```

#### Property Value

[ElementId](../Autodesk.Revit.DB/Element-Id-Class.md) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The startSymbolTypeId is not a valid start symbol or arrowhead type. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[StairsPathType Class](36994970-3d80-62a3-df6f-381d38f2eda0.htm) [Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)
