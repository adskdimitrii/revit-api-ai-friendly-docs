# Family Is Parametric Property

Source: https://www.revitapidocs.com/2026/1d4166dd-057d-9d9b-e28f-7bd250bbe587.htm

---

| Family Is Parametric Property |
| --- |

Identifies whether the family contains parametric relations
 between some of its elements. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public bool IsParametric { get; }
```

```
Public ReadOnly Property IsParametric As Boolean
	Get
```

```
public:
property bool IsParametric {
	bool get ();
}
```

```
member IsParametric : bool with get
```

#### Property Value

Boolean ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks A family is parametric if it contains parameter\-driven relations between
 its elements, such as labeled dimensions or locked tangential joins. 

Parametric families containing large sketches may cause performance
 problems. Caution is therefore advised before adding any constraints to
 a yet non\-parametric family that already contains large sketches.
 See [HasLargeSketches](c49820d6-d8f2-de9a-544d-f896a32e39c8.htm) . 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Family Class](f51d019d-6ff3-692b-d1d2-b497cab564de.htm) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
