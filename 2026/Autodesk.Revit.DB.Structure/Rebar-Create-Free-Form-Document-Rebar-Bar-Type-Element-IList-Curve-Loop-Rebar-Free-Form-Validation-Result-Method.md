# Rebar Create Free Form(Document, Rebar Bar Type, Element, IList Curve Loop , Rebar Free Form Validation Result ) Method

Source: https://www.revitapidocs.com/2026/38767c5e-0196-3359-69db-19d728873b19.htm

---

| Rebar Create Free Form(Document, Rebar Bar Type, Element, IList Curve Loop , Rebar Free Form Validation Result ) Method |
| --- |

**Note: This API is now obsolete.** 

  
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use Rebar.CreateFreeForm(Document doc, RebarBarType barType, Element host, IList(CurveLoop) curves, RebarStyle style) instead.")]
public static Rebar CreateFreeForm(
	Document doc,
	RebarBarType barType,
	Element host,
	IList<CurveLoop> curves,
	out RebarFreeFormValidationResult error
)
```

```
<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use Rebar.CreateFreeForm(Document doc, RebarBarType barType, Element host, IList(CurveLoop) curves, RebarStyle style) instead.")>
Public Shared Function CreateFreeForm ( 
	doc As Document,
	barType As RebarBarType,
	host As Element,
	curves As IList(Of CurveLoop),
	<OutAttribute> ByRef error As RebarFreeFormValidationResult
) As Rebar
```

```
public:
[ObsoleteAttribute(L"This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use Rebar.CreateFreeForm(Document doc, RebarBarType barType, Element host, IList(CurveLoop) curves, RebarStyle style) instead.")]
static Rebar^ CreateFreeForm(
	Document^ doc, 
	RebarBarType^ barType, 
	Element^ host, 
	IList<CurveLoop^>^ curves, 
	[OutAttribute] RebarFreeFormValidationResult% error
)
```

```
[<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use Rebar.CreateFreeForm(Document doc, RebarBarType barType, Element host, IList(CurveLoop) curves, RebarStyle style) instead.")>]
static member CreateFreeForm : 
        doc : Document * 
        barType : RebarBarType * 
        host : Element * 
        curves : IList<CurveLoop> * 
        error : RebarFreeFormValidationResult byref -> Rebar 
```

#### Parameters

doc [Document](../Autodesk.Revit.DB/Document-Class.md)
barType [RebarBarType](Rebar-Bar-Type-Class.md)
host [Element](../Autodesk.Revit.DB/Element-Class.md)
curves IList [CurveLoop](84824924-cb89-9e20-de6e-3461f429dfd6.htm)
error [RebarFreeFormValidationResult](def069dd-2e03-7b93-6482-9bf28c70e7ed.htm)

#### Return Value

[Rebar](Rebar-Class.md) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Rebar Class](Rebar-Class.md) [CreateFreeForm Overload](Rebar-Create-Free-Form-Method.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
