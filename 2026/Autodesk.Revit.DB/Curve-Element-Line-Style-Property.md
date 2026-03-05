# Curve Element Line Style Property

Source: https://www.revitapidocs.com/2026/691e64a2-e5ea-b619-4362-1a2c17e23b2f.htm

---

| Curve Element Line Style Property |
| --- |

The line style of this curve element. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public Element LineStyle { get; set; }
```

```
Public Property LineStyle As Element
	Get
	Set
```

```
public:
property Element^ LineStyle {
	Element^ get ();
	void set (Element^ value);
}
```

```
member LineStyle : Element with get, set
```

#### Property Value

[Element](Element-Class.md) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when argument is . |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when regeneration failed. \-\- or \-\- Thrown when fail to get line style. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks The return of this property will be a \[!:Autodesk::Revit::DB::GraphicsStyle] element.
These graphics styles should be associated to subcategories of the BuiltInCategory OST\_Lines. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[CurveElement Class](61673852-2d08-003d-e9fd-4be89d533774.htm) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
