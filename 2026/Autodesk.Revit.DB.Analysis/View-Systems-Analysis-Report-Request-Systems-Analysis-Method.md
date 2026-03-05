# View Systems Analysis Report Request Systems Analysis Method

Source: https://www.revitapidocs.com/2026/b36cb95e-9857-9028-4587-86fdb6767cbc.htm

---

| View Systems Analysis Report Request Systems Analysis Method |
| --- |

Requests a new systems analysis to be run in the background. 
**Namespace:** [Autodesk.Revit.DB.Analysis](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void RequestSystemsAnalysis(
	SystemsAnalysisOptions options
)
```

```
Public Sub RequestSystemsAnalysis ( 
	options As SystemsAnalysisOptions
)
```

```
public:
void RequestSystemsAnalysis(
	SystemsAnalysisOptions^ options
)
```

```
member RequestSystemsAnalysis : 
        options : SystemsAnalysisOptions -> unit 
```

#### Parameters

options [SystemsAnalysisOptions](8d8fe6a8-d3f6-c4fd-99ac-3181ba0253d6.htm)
:   The additional options to run systems analysis. If empty, use the default value in the view element.
 The request may download the weather file at current site location if not specified in the options.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ArgumentsInconsistentException](05972c68-fa6d-3a83-d720-ad84fbc4780f.htm) | No weather station is within 500 nautical miles of this site location. |
| [FileNotFoundException](73250198-dbc6-e760-4297-ec062f00f574.htm) | Fail to download the weather file. |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | A valid energy model is required for systems analysis.  \-or\-  Unable to export the gbxml file or access the weather service. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks Should be called from a transaction. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[ViewSystemsAnalysisReport Class](View-Systems-Analysis-Report-Class.md) [Autodesk.Revit.DB.Analysis Namespace](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md)
